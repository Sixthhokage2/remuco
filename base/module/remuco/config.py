# =============================================================================
#
#    Remuco - A remote control system for media players.
#    Copyright (C) 2006-2010 by the Remuco team, see AUTHORS.
#
#    This file is part of Remuco.
#
#    Remuco is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Remuco is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Remuco.  If not, see <http://www.gnu.org/licenses/>.
#
# =============================================================================

import ConfigParser
from ConfigParser import NoOptionError
import os
import os.path
from os.path import join as opj
import shutil
import sys

from remuco import log
from remuco import defs
from remuco.remos import user_config_dir
from remuco.remos import user_cache_dir

DEVICE_FILE = opj(user_cache_dir, "remuco", "devices")

SEC = ConfigParser.DEFAULTSECT

CONFIG_VERSION_MAJOR = "2"
CONFIG_VERSION_MINOR = "0"
CONFIG_VERSION = "%s.%s" % (CONFIG_VERSION_MAJOR, CONFIG_VERSION_MINOR)

KEY_CONFIG_VERSION = "config-version"
KEY_BLUETOOTH = "bluetooth-enabled"
KEY_BLUETOOTH_CHAN = "bluetooth-channel"
KEY_WIFI = "wifi-enabled"
KEY_WIFI_PORT = "wifi-port"
KEY_ENDCODING = "player-encoding"
KEY_LOGLEVEL = "log-level"
KEY_FB_SHOW_EXT = "file-browser-show-extensions"
KEY_FB_ROOT_DIRS = "file-browser-root-dirs"
KEY_MPRIS_JUMP = "mpris-jump"

DEFAULTS = { # values as saved in config file
    KEY_BLUETOOTH: "1",
    KEY_BLUETOOTH_CHAN: "0",
    KEY_WIFI: "1",
    KEY_WIFI_PORT: "34271",
    KEY_ENDCODING: "UTF8",
    KEY_LOGLEVEL: "INFO",
    KEY_FB_SHOW_EXT: "0",
    KEY_FB_ROOT_DIRS: "auto",
    KEY_MPRIS_JUMP: "0" }

class Config(object):
    """Class for getting and setting player adapter specific configurations.
    
    An instance of Config mirrors the configuration of a specific player
    adapter (usually ~/.config/remuco/PLAYER/conf). Any change to the
    properties of an instance of Config automatically gets saved in the
    configuration file.
    
    In most cases player adapters do not need this. It is useful if a player
    adapter wants to provide a UI to configure the adapter.
    
    Player adapters are not supposed to create instances of Config. Instead
    use the property 'config' of PlayerAdapter to access the currently used
    Config instance.
    
    """
    
    def __init__(self, player_name):
        """Do not use this. Use PlayerAdapter.config instead."""
        
        self.__name = player_name
        
        ###### init directories and file names ######
        
        # convert descriptive name to a plain canonical one
        name_plain = player_name.lower().replace(" ", "").replace(".","")
        
        self.__dir_config = opj(user_config_dir, "remuco", name_plain)
        self.__dir_cache = opj(user_cache_dir, "remuco", name_plain)
        self.__file_config = opj(self.__dir_config, "conf")
        self.__file_log = opj(self.__dir_cache, "log")
    
        try:
            if not os.path.isdir(self.__dir_config):
                os.makedirs(self.__dir_config)
            if not os.path.isdir(self.__dir_cache):
                os.makedirs(self.__dir_cache)
        except OSError, e:
            log.error("failed to make dir: %s", e)
        else:
            if not "--remuco-log-stdout" in sys.argv:
                log.set_file(self.__file_log)
        
        ###### custom volume command ######
        
        cmd = opj(user_config_dir, "remuco", "volume")
        if not os.path.isfile(cmd):
            cmd = opj(self.__dir_config, "volume")
        if not os.path.isfile(cmd):
            log.debug("custom volume command does not exist (%s)" % cmd)
            self.__custom_volume_cmd = None
        elif not os.access(cmd, os.X_OK):
            log.warning("custom volume command (%s) is not executable" % cmd)
            self.__custom_volume_cmd = None
        else:
            log.info("using custom volume command (%s)" % cmd)
            self.__custom_volume_cmd = cmd
        
        ###### load configuration ######
        
        self.__cp = ConfigParser.SafeConfigParser(DEFAULTS)

        if os.path.exists(self.__file_config):
            self.__load() 
            self.__check_version()
        else:
            self.__cp.set(SEC, KEY_CONFIG_VERSION, CONFIG_VERSION)
            self.__save()

        log.set_level(self.log_level)
        
        log.info("remuco version: %s" % defs.REMUCO_VERSION)
        
    def __check_version(self):
        """Check version of the configuration.
        
        Resets the config on a major change and rewrites the config on any
        change. The last ensures that added options (minor change) are present
        in the configuration file.
        
        """
        try: # check version
            version = self.__cp.get(SEC, KEY_CONFIG_VERSION)
        except (ValueError, AttributeError, NoOptionError):
            version = "0.0"

        major = version.split(".")[0]

        if major != CONFIG_VERSION_MAJOR:
            # on major change, reset configuration
            old_config = "%s.old" % self.__file_config
            log.info("config major version changed -> reset (backup: %s)" %
                     old_config)
            shutil.copy(self.__file_config, old_config)
            self.__cp = ConfigParser.SafeConfigParser(DEFAULTS)
            
        # remove old, now unused options:
        
        rewrite = False
        items = self.__cp.items(SEC)
        for key, val in items:
            if not (key in DEFAULTS or key.startswith("custom-") or
                    key == KEY_CONFIG_VERSION):
                # obsolete option -> remove
                self.__cp.remove_option(SEC, key)
                rewrite = True

        # force a rewrite if something has changed
        
        if version != CONFIG_VERSION or rewrite:
            # on any change (major or minor), rewrite config
            log.debug("config structure changed -> force rewrite")
            self.__cp.set(SEC, KEY_CONFIG_VERSION, CONFIG_VERSION)
            self.__save()

    def __load(self):

        log.debug("try to load config from %s" % self.__file_config)
        
        try:
            self.__cp.read(self.__file_config)
        except ConfigParser.Error, e:
            log.warning("failed to read config from %s (%s) -> %s" %
                        (self.__file_config, e, "using defaults"))
        
    def __save(self):
        
        try:
            self.__cp.write(open(self.__file_config, 'w'))
        except IOError, e:
            log.warning("failed to save config to %s (%s)" %
                        (self.__file_config, e))

    # === custom options ===

    def get_custom(self, option, default):
        """Get the value of a custom configuration option.
        
        @param option: name of the option
        
        @see: set_custom()
        
        """
        try:
            return self.__cp.get(SEC, "custom-%s" % option)
        except (ValueError, AttributeError), e:
            log.warning("config '%s' malformed (%s)" % (option, e))
            return default
        except ConfigParser.NoOptionError:
            return default

    def set_custom(self, option, value):
        """Set the value of a custom configuration option.
        
        Using this method, player adapters may integrate additional
        configuration options in the adapter's configuration file.
        
        @param option: name of the option
        
        @note: Internally this is saved as "custom-<OPTION>".
        
        """
        self.__cp.set(SEC, "custom-%s" % option, str(value))
        self.__save()

    # === property: bluetooth ===
    
    def __pget_bluetooth(self):
        """Flag if Bluetooth is enabled.
        
        Default: True (enabled)
        
        Option name: 'bluetooth-enabled'
        
        """
        try:
            return self.__cp.getboolean(SEC, KEY_BLUETOOTH)
        except (ValueError, AttributeError), e:
            log.warning("config '%s' malformed (%s)" % (KEY_BLUETOOTH, e))
            return True
    
    def __pset_bluetooth(self, value):
        
        self.__cp.set(SEC, KEY_BLUETOOTH, str(value))
        self.__save()
        
    bluetooth = property(__pget_bluetooth, __pset_bluetooth, None,
                         __pget_bluetooth.__doc__)

    # === property: bluetooth_channel ===
    
    def __pget_bluetooth_channel(self):
        """Channel to use for Bluetooth connections.
        
        Default: 0 (select channel automatically)
        
        Option name: 'bluetooth-channel'
        """
        try:
            return self.__cp.getint(SEC, KEY_BLUETOOTH_CHAN)
        except (ValueError, AttributeError), e:
            log.warning("config '%s' malformed (%s)" % (KEY_BLUETOOTH_CHAN, e))
            return 0
    
    def __pset_bluetooth_channel(self, value):
        
        self.__cp.set(SEC, KEY_BLUETOOTH_CHAN, str(value))
        self.__save()
    
    bluetooth_channel = property(__pget_bluetooth_channel,
                                 __pset_bluetooth_channel, None,
                                 __pget_bluetooth_channel.__doc__)
    
    # === property: wifi ===
    
    def __pget_wifi(self):
        """Flag if WiFi/Inet is enabled.
        
        Default: True (enabled)
        
        Option name: 'wifi-enabled'
        
        """
        try:
            return self.__cp.getboolean(SEC, KEY_WIFI)
        except (ValueError, AttributeError), e:
            log.warning("config '%s' malformed (%s)" % (KEY_WIFI, e))
            return True
    
    def __pset_wifi(self, value):
        
        self.__cp.set(SEC, KEY_WIFI, str(value))
        self.__save()
    
    wifi = property(__pget_wifi, __pset_wifi, None, __pget_wifi.__doc__)
    
    # === property: wifi_port ===
    
    def __pget_wifi_port(self):
        """Port to use for WiFi connections.
        
        Default: 34271
        
        Option name: 'wifi-port'

        """
        try:
            return self.__cp.getint(SEC, KEY_WIFI_PORT)
        except (ValueError, AttributeError), e:
            log.warning("config '%s' malformed (%s)" % (KEY_WIFI_PORT, e))
            return 34271
        
    def __pset_wifi_port(self, value):

        self.__cp.set(SEC, KEY_WIFI_PORT, str(value))
        self.__save()
    
    wifi_port = property(__pget_wifi_port, __pset_wifi_port, None,
                         __pget_wifi_port.__doc__)

    # === property: encoding ===
    
    def __pget_encoding(self):
        """Encoding of strings coming from and passed to the player (adapter).
        
        Default: 'UTF-8'
        
        Option name: 'player-encoding'
        
        """
        try:
            return self.__cp.get(SEC, KEY_ENDCODING)
        except (ValueError, AttributeError), e:
            log.warning("config '%s' malformed (%s)" % (KEY_ENDCODING, e))
            return "UTF8"
    
    def __pset_encoding(self, value):
        
        self.__cp.set(SEC, KEY_ENDCODING, str(value))
        self.__save()
    
    encoding = property(__pget_encoding, __pset_encoding, None,
                        __pget_encoding.__doc__)

    # === property: log_level ===
    
    def __pget_log_level(self):
        """Log level to use.
        
        Default: log.INFO
        Possible values: log.DEBUG, log.INFO, log.WARNING, log.ERROR
        
        Option name: 'log-level'
        """
        try:
            val = self.__cp.get(SEC, KEY_LOGLEVEL)
        except (ValueError, AttributeError,), e:
            log.warning("config '%s' malformed (%s)" % (KEY_LOGLEVEL, e))
            val = "INFO"
        
        level_map = {"DEBUG": log.DEBUG, "INFO": log.INFO,
                     "WARNING": log.WARNING, "ERROR": log.ERROR }
        try:
            return level_map[val]
        except KeyError:
            log.warning("config '%s' has invalid value" % KEY_LOGLEVEL)
            return log.INFO
    
    def __pset_log_level(self, value):
        
        if value in ("DEBUG", "INFO", "WARNING", "ERROR"):
            level = value
        elif value == log.DEBUG: 
            level = "DEBUG"
        elif value == log.INFO:
            level = "ERROR"
        elif value == log.WARNING:
            level = "ERROR"
        elif value == log.ERROR:
            level = "ERROR"
        else:
            log.error("** BUG ** unsupported log level: %s" % str(value))
            level = "INFO"
            
        self.__cp.set(SEC, KEY_LOGLEVEL, level)
        self.__save()
    
    log_level = property(__pget_log_level, __pset_log_level, None,
                         __pget_log_level.__doc__)

    # === property: fb_extensions ===
    
    def __pget_fb_extensions(self):
        """Flag if file browser shows file name extensions.
        
        Default: False (hide extensions)
        
        Option name: 'file-browser-show-extensions'
        
        """
        try:
            return self.__cp.getboolean(SEC, KEY_FB_SHOW_EXT)
        except (ValueError, AttributeError), e:
            log.warning("config '%s' malformed (%s)" % (KEY_FB_SHOW_EXT, e))
            return False
    
    def __pset_fb_extensions(self, value):
    
        self.__cp.set(SEC, KEY_FB_SHOW_EXT, str(value))
        self.__save()
    
    fb_extensions = property(__pget_fb_extensions, __pset_fb_extensions, None,
                             __pget_fb_extensions.__doc__)

    # === property: root_dirs ===
    
    def __pget_fb_root_dirs(self):
        """List of directories to show as root directories in the file browser.
        
        The reserved directory name `auto` will be replaced by directories
        containing media of the mimetypes defined in a player adapter.
        
        Default: ["auto"]
        
        Option name: 'file-browser-root-dirs'
        
        """
        try:
            val = self.__cp.get(SEC, KEY_FB_ROOT_DIRS)
        except (ValueError, AttributeError), e:
            log.warning("config '%s' malformed (%s)" % (KEY_ENDCODING, e))
            val = None

        if not val:
            return []
        
        roots = val.split(os.path.pathsep)
        stripped = []
        for root_dir in roots:
            if root_dir:
                stripped.append(root_dir.strip())
        return stripped
    
    def __pset_fb_root_dirs(self, value):
        
        roots = ""
        if value:
            for root_dir in value:
                roots = "%s%s%s" % (roots, os.path.pathsep, root_dir)
            roots = roots[1:]

        self.__cp.set(SEC, KEY_FB_ROOT_DIRS, roots)
        self.__save()
    
    fb_root_dirs = property(__pget_fb_root_dirs, __pset_fb_root_dirs, None,
                            __pget_fb_root_dirs.__doc__)

    # === propety: mpris-jump ===

    def __pget_mprisjump(self):
        """Flag if mpris-jump is enabled.

        Default: 0 (disabled)

        Option name: 'mpris-jump'

        """
        try:
            return self.__cp.getboolean(SEC, KEY_MPRIS_JUMP)
        except (ValueError, AttributeError), e:
            log.warning("config '%s' malformed (%s)" % (KEY_MPRIS_JUMP, e))
            return False

    def __pset_mprisjump(self, value):

        self.__cp.set(SEC, KEY_MPRIS_JUMP, str(value))
        self.__save()

    mprisjump = property(__pget_mprisjump, __pset_mprisjump, None, 
                         __pget_mprisjump.__doc__)

    # === property: config_dir ===
    
    def __pget_config_dir(self):
        """Player adapter specific configuration directory.
        
        Usually this is ~/.config/remuco/PLAYER.
        
        @note: read-only

        """
        return self.__dir_config
    
    config_dir = property(__pget_config_dir, None, None,
                          __pget_config_dir.__doc__)

    # === property: cache_dir ===
    
    def __pget_cache_dir(self):
        """Player adapter specific configuration directory.
        
        Usually this is ~/.cache/remuco/PLAYER.
        
        @note: read-only
        
        """
        return self.__dir_cache
    
    cache_dir = property(__pget_cache_dir, None, None,
                         __pget_cache_dir.__doc__)

    # === property: log_file ===
    
    def __pget_log_file(self):
        """Player adapter specific log file.
        
        Usually this is ~/.cache/remuco/PLAYER/log.
        
        @attention: Do not use this for writing log messages to (use
            remuco.log.debug() and friends). This property may be useful for
            player adapters integrating log information in a UI.

        @note: read-only

        """
        return self.__file_log
    
    log_file = property(__pget_log_file, None, None, __pget_log_file.__doc__)
    
    # === property: custom_volume_cmd ===
    
    def __pget_custom_volume_cmd(self):
        """Used internally (read-only)"""
        return self.__custom_volume_cmd
    
    custom_volume_cmd = property(__pget_custom_volume_cmd, None, None,
                                 __pget_custom_volume_cmd.__doc__)


def get_system_shutdown_command():
        
    path = opj(user_config_dir, "remuco", "shutdown-system")
    
    if not os.path.isfile(path):
        log.info("system shutdown disabled")
        return None
    
    if not os.access(path, os.X_OK):
        log.info("system shutdown command (%s) is not executable" % path)
        return None
    
    log.info("system shutdown enabled")
    
    return path

__all__ = (Config,)

