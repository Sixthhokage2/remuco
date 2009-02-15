package remuco.ui.screens;

import java.util.Vector;

import javax.microedition.lcdui.Alert;
import javax.microedition.lcdui.AlertType;
import javax.microedition.lcdui.Command;
import javax.microedition.lcdui.CommandListener;
import javax.microedition.lcdui.Display;
import javax.microedition.lcdui.Displayable;
import javax.microedition.lcdui.Image;
import javax.microedition.lcdui.List;

import remuco.Config;
import remuco.UserException;
import remuco.comm.BluetoothFactory;
import remuco.comm.IDeviceSelectionListener;
import remuco.comm.IScanListener;
import remuco.comm.IScanner;
import remuco.ui.CMD;
import remuco.ui.CommandList;
import remuco.ui.Theme;
import remuco.util.Log;

public final class DeviceSelectorScreen extends List implements
		CommandListener, IScanListener {

	private static final Command CMD_ADD_BLUETOOTH = new Command("Bluetooth",
			Command.SCREEN, 10);

	private static final Command CMD_ADD_INET = new Command("WiFi",
			Command.SCREEN, 20);

	private static final Command CMD_CONNECT = new Command("Select",
			Command.SCREEN, 1);

	private static final Command CMD_REMOVE_DEVICE = new Command(
			"Remove Connection", Command.SCREEN, 30);

	/** Add command for the scan result list. */
	private static final Command CMD_SCAN_RESULT_ADD = new Command("Add",
			Command.SCREEN, 1);

	private final Alert alertScanProblem, alertForgetDevice;

	private final IScanner bluetoothScanner;

	/**
	 * Contains the devices currently selectable by the user. Element
	 * <code>3 * i</code> is the address of device <code>i</code>, element
	 * <code>3 * i + 1</code> its name and element <code>3 * i + 2</code> its
	 * type (one of {@link Config#DEVICE_TYPE_BLUETOOTH} or
	 * {@link Config#DEVICE_TYPE_INET}).
	 */
	private String[] devices = new String[0];

	private final Display display;

	private final IDeviceSelectionListener listener;

	private final CommandListener parent;

	private String scanResults[] = new String[0];

	private final AddInetDeviceScreen screenAddInetDevice;

	private final CommandList screenDeviceTypeSelection;

	private final WaitingScreen screenScanning;

	private final List screenScanResults;

	public DeviceSelectorScreen(CommandListener parent, Display display,
			IDeviceSelectionListener listener) {

		super("Connections", IMPLICIT);

		this.parent = parent;
		this.display = display;
		this.listener = listener;

		if (BluetoothFactory.BLUETOOTH) {
			bluetoothScanner = BluetoothFactory.createBluetoothScanner();
		} else {
			bluetoothScanner = null;
		}

		alertScanProblem = new Alert("");
		alertScanProblem.setType(AlertType.ERROR);
		alertScanProblem.setTimeout(Alert.FOREVER);
		alertScanProblem.setCommandListener(this);

		alertForgetDevice = new Alert("Confirmation");
		alertForgetDevice.setString("Please confirm ..");
		alertForgetDevice.setType(AlertType.WARNING);
		alertForgetDevice.setTimeout(Alert.FOREVER);
		alertForgetDevice.addCommand(CMD.NO);
		alertForgetDevice.addCommand(CMD.YES);
		alertForgetDevice.setCommandListener(this);

		screenAddInetDevice = new AddInetDeviceScreen();
		screenAddInetDevice.addCommand(CMD.BACK);
		screenAddInetDevice.addCommand(CMD.OK);
		screenAddInetDevice.setCommandListener(this);

		screenDeviceTypeSelection = new CommandList("Add Connection", CMD.OK);
		screenDeviceTypeSelection.addCommand(CMD.BACK);
		if (bluetoothScanner != null) {
			screenDeviceTypeSelection.addCommand(CMD_ADD_BLUETOOTH,
					Theme.LIST_ICON_BLUETOOTH);
		}
		screenDeviceTypeSelection
				.addCommand(CMD_ADD_INET, Theme.LIST_ICON_WIFI);
		screenDeviceTypeSelection.setCommandListener(this);

		screenScanning = new WaitingScreen();
		screenScanning.setTitle("Scanning");
		screenScanning.setImage(Theme.ALERT_ICON_BLUETOOTH);
		screenScanning.setMessage("Searching for Bluetooth devices.");
		screenScanning.setCommandListener(this);

		screenScanResults = new List("Scan Results", List.IMPLICIT);
		screenScanResults.addCommand(CMD.BACK);
		screenScanResults.addCommand(CMD_SCAN_RESULT_ADD);
		screenScanResults.setCommandListener(this);

		addCommand(CMD_CONNECT);
		setSelectCommand(CMD_CONNECT);
		setCommandListener(this);
	}

	public void commandAction(Command c, Displayable d) {

		if (c.equals(CMD_CONNECT)) { // DEVICE SELECTED //

			final int index = getSelectedIndex();

			if (index < 0) {
				return;
			}

			if (index == size() - 1) { // add connection

				display.setCurrent(screenDeviceTypeSelection);
				return;
			}

			final String addr = devices[3 * index];
			final String name = devices[3 * index + 1];
			final String type = devices[3 * index + 2];

			// remember the device
			Config.knownDevicesAdd(addr, name, type);

			listener.notifySelectedDevice(type, addr);

		} else if (c == WaitingScreen.CMD_CANCEL) { // cancel scan

			bluetoothScanner.cancelScan();

			display.setCurrent(this);

		} else if (c == CMD.BACK && d == screenDeviceTypeSelection) {

			display.setCurrent(this);

		} else if (c == CMD_ADD_BLUETOOTH) {

			try {
				bluetoothScanner.startScan(this);
				display.setCurrent(screenScanning);
			} catch (UserException e) {
				alertScanProblem.setTitle("Scan Error");
				alertScanProblem
						.setString(e.getError() + ": " + e.getDetails());
				alertScanProblem.setType(AlertType.ERROR);
				display.setCurrent(alertScanProblem, this);
			}

		} else if (c == CMD_ADD_INET) {

			display.setCurrent(screenAddInetDevice);

		} else if (c == CMD.OK && d == screenAddInetDevice) {

			final String address = screenAddInetDevice.getAddress();

			if (address == null) {
				final Alert alert = new Alert("Error", "Invalid host!", null,
						AlertType.ERROR);
				display.setCurrent(alert, screenAddInetDevice);
				return;
			}

			Config.knownDevicesAdd(address, null, Config.DEVICE_TYPE_INET);

			update();

			display.setCurrent(this);

		} else if (c == CMD.BACK && d == screenAddInetDevice) {

			display.setCurrent(this);

		} else if (c == CMD.BACK && d == screenScanResults) {

			display.setCurrent(this);

		} else if (c == CMD_SCAN_RESULT_ADD) {

			final int index = screenScanResults.getSelectedIndex();

			if (index == -1) {
				return;
			}

			final String addr = scanResults[3 * index];
			final String name = scanResults[3 * index + 1];
			final String type = scanResults[3 * index + 2];

			Config.knownDevicesAdd(addr, name, type);

			update();

			display.setCurrent(this);

		} else if (c == CMD_REMOVE_DEVICE) {

			alertForgetDevice.setString("Remove connection "
					+ getString(getSelectedIndex()) + " ?");

			display.setCurrent(alertForgetDevice);

		} else if (c == CMD.NO && d == alertForgetDevice) {

			display.setCurrent(this);

		} else if (c == CMD.YES && d == alertForgetDevice) {

			final int index = getSelectedIndex();

			if (index < 0) {
				return;
			}

			Config.knownDevicesDelete(devices[3 * index]);

			update();

			display.setCurrent(this);

		} else if (c == Alert.DISMISS_COMMAND) {

			display.setCurrent(this);

		} else {

			parent.commandAction(c, d); // includes LOG
		}
	}

	public void notifyScannedDevices(String[] devs) {

		if (devs.length == 0) {
			alertScanProblem.setTitle("No Devices");
			alertScanProblem.setString("Please check if your computer is in "
					+ "range, its Bluetooth is enabled and visible.");
			display.setCurrent(alertScanProblem, this);

			return;
		}

		scanResults = devs;

		screenScanResults.deleteAll();

		for (int i = 0; i < devs.length; i += 3) {

			final String name = devs[i + 1] != null ? devs[i + 1] : devs[i];

			final Image icon;

			if (devs[i + 2].equals(Config.DEVICE_TYPE_BLUETOOTH)) {
				icon = Theme.LIST_ICON_BLUETOOTH;
			} else if (devs[i + 2].equals(Config.DEVICE_TYPE_INET)) {
				icon = Theme.LIST_ICON_WIFI;
			} else {
				Log.bug("Jan 28, 2009.10:57:37 PM");
				icon = null;
			}

			screenScanResults.append(name, icon);
		}

		display.setCurrent(screenScanResults);
	}

	/**
	 * On first time display, use this method instead of
	 * {@link Display#setCurrent(Displayable)}.
	 */
	public void showYourself() {

		update();

		if (devices.length == 0) {
			if (BluetoothFactory.BLUETOOTH) {
				display.setCurrent(screenDeviceTypeSelection);
			} else {
				final Alert alert = new Alert("No Bluetooth",
						"Bluetooth is not available. "
								+ "Only Wifi connections are possible.",
						Theme.ALERT_ICON_WIFI, AlertType.INFO);
				display.setCurrent(alert, screenAddInetDevice);
			}
		} else
			display.setCurrent(this);

	}

	/**
	 * Update list to show all known devices. As a side effect, {@link #devices}
	 * gets updated to the devices returned by {@link Config#knownDevicesGet()}.
	 */
	private void update() {

		final Vector knownDevs = Config.knownDevicesGet();

		devices = new String[knownDevs.size()];

		knownDevs.copyInto(devices);

		if (devices.length > 0) {
			addCommand(CMD_REMOVE_DEVICE);
		} else {
			removeCommand(CMD_REMOVE_DEVICE);
		}

		deleteAll();

		for (int i = 0; i < devices.length; i += 3) {

			final String name = devices[i + 1] != null ? devices[i + 1]
					: devices[i];

			final Image icon;

			if (devices[i + 2].equals(Config.DEVICE_TYPE_BLUETOOTH)) {
				icon = Theme.LIST_ICON_BLUETOOTH;
			} else if (devices[i + 2].equals(Config.DEVICE_TYPE_INET)) {
				icon = Theme.LIST_ICON_WIFI;
			} else {
				Log.bug("Jan 28, 2009.10:57:37 PM");
				icon = null;
			}

			append(name, icon);
		}

		append("Add", Theme.LIST_ICON_ADD);

		setSelectedIndex(0, true);
	}

}