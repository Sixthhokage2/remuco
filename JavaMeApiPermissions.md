

The most important first: On devices operated by _AT&T Wireless_ or _T-Mobile U.S._ Remuco is likely to fail because it is not allowed to use the APIs it needs (network and Bluetooth connections). Usually users have a chance to adjust permissions per applications, but on phones of these operators this is not possible.

# Remuco and permissions #

  * Remuco requires the permissions
    * <tt>javax.microedition.io.Connector.socket</tt> for WiFi connections and
    * <tt>javax.microedition.io.Connector.bluetooth.client</tt> for Bluetooth connections.
  * [Here is a list of issues related to JavaME API permissions](http://code.google.com/p/remuco/issues/list?can=1&q=label:Permissions).

# Technical information #

  * [Domain policies of some carriers that deviate from the standard](http://wiki.forum.nokia.com/index.php/Java_Security_Domains#Security_Domain_policies_some_carriers_that_deviate_from_the_standardSecurity)
  * Short link to check if your operator may prevent Remuco from setting up connections.

  * [AT&T developer board discussion](http://developerboards.att.lithium.com/cngddp/board/message?message.uid=26105)
  * An AT&T moderator states that Bluetooth connections are only allowed to applications signed by AT&T.

  * [AT&T Java Signing Specification](http://developer.att.com/developer/index.jsp?page=toolsTechDetail&id=11300207)
  * Lists API access rights for phones operated by AT&T.
  * Access to the APIs required by Remuco is not allowed.

  * [T-Mobile U.S. API access rights](http://wiki.forum.nokia.com/index.php/T-Mobile_U.S._API_access_rights)
  * Lists API access rights for phones operated by T-Mobile U.S.
  * Access to the APIs required by Remuco is not allowed.

  * [Nokia API access rights](http://wiki.forum.nokia.com/index.php/Java_Security_Domains)
  * Plenty of information about general MIDP and Nokia specific permission settings as well as some information about permissions used by other manufacturers and operators.

  * [Discussion about N96 an N80 permission settings](http://discussion.forum.nokia.com/forum/showthread.php?t=149334) (for signed apps)

  * [Sprint API access rights](http://developer.sprint.com/getDocument.do?docId=91801) → page 16
  * WiFi connections seem to work, Bluetooth connections may fail.
  * Required permissions need to be declared in the descriptor file ([Customization#Adjust\_permission\_settings here is how to do that](Client.md)).

# Blog posts and other discussions #

  * [vufone blog - CTO Corner: Java Micro Edition in a Nutshell](http://blog.vufone.com/tag/j2me-permissions/)
  * Addresses the issue that unsigned JavaME application (like most [FOSS](http://en.wikipedia.org/wiki/FOSS)) fail to work on devices from certain manufacturers or operators due to restrictive API access rights.
  * Excerpt: "_The most painful aspect of deploying Java ME applications is the issue of signatures. There are several operations which require permissions, such as accessing the network, reading and writing user data, sending SMS, and others. APIs that provide access to these operations are restricted and the application will be allowed to use them only if the application manager grants the relevant permissions. [...] Furthermore, some devices allow only applications in the operator or manufacturer domain to accebe a problem to usess certain operations. It means that as a third party developer you may not be able to install your application on these phones._"

  * [Javablog: How MIDlet Signing is Killing J2ME](http://javablog.co.uk/2007/08/09/how-midlet-signing-is-killing-j2me/)
  * Another developer pointing to the limited API access rights issue for unsigned JavaME applications.

  * [SpencerUresk: The hidden problem with J2ME](http://www.spenceruresk.com/2007/05/26/the-hidden-problem-with-j2me/)
  * And one more blog post, similar to the one above.