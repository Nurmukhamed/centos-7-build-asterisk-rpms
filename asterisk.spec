# TODO:
# - chan_misdn (BR: mISDNuser-devel 1.x, needs update for 2.0)
# - ffmpeg: sws_getContext now in libswscale, not avcodec
# - gmime: reverse version check order, use gmime-2.6 by default
# - nbs (libnbs, nbs.h)
# - ss7 >= 2.0 (libss7, libssh.h)
# - openr2 (libopenr2, libopenr2.h)
# - pwlib+openh323
# - vpb (libvpb, vpbapi.h)
# - make package for moh sound files
# - build res_ari_mailboxes as an alternative for voicemail subpackages
# - +x missing:
#   ldd: warning: you do not have execution permission for `/usr/lib/libasteriskssl.so.1'
#
# Conditional build:
Summary:	Asterisk PBX
Name:		asterisk
Version:	14.6.1
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	https://downloads.asterisk.org/pub/telephony/asterisk/releases/%{name}-%{version}.tar.gz
# Source0-md5:	d980162e8a7be13fd85dbab81e7d0bfe
Source2:	%{name}.sysconfig
Source3:	%{name}.tmpfiles
Source4:	%{name}.logrotate
Source5:	%{name}.service
# menuselect.* -> make menuconfig; choose options; copy resulting files here
Source6:	menuselect.makedeps
Source7:	menuselect.makeopts
URL:		http://www.asterisk.org/
BuildRequires:	autoconf 
BuildRequires:	automake
BuildRequires:	bison 
BuildRequires:	doxygen
BuildRequires:	flex
BuildRequires:	gawk
BuildRequires:  gcc
BuildRequires:	gmime-devel
BuildRequires:	iksemel-devel
BuildRequires:	jansson-devel
BuildRequires:	libcap-devel
BuildRequires:	libedit-devel
BuildRequires:	gsm-devel
BuildRequires:	libical-devel
BuildRequires:	libogg-devel
BuildRequires:	libtiff-devel
BuildRequires:	libuuid-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libxml2-devel 
BuildRequires:	libxslt-devel
BuildRequires:	ncurses-devel
BuildRequires:	neon-devel
BuildRequires:	net-snmp-devel
BuildRequires:	newt-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pam-devel
%{?with_pjsip:BuildRequires:	pjproject-devel >= 2.3}
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	rpm-build
BuildRequires:	sed >= 4.0
BuildRequires:	spandsp-devel >= 0.0.5
BuildRequires:	speex-devel
%{?with_sqlite2:BuildRequires:	sqlite-devel >= 2}
BuildRequires:	sqlite-devel
BuildRequires:	libsrtp-devel
Requires(post,preun,postun):	systemd-units >= 38
Requires:	systemd-units >= 0.38
BuildRequires:	uriparser-devel
BuildRequires:	zlib-devel
BuildRequires:	gcc-c++
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(pre):	/usr/bin/getent
Provides:	group(asterisk)
Provides:	user(asterisk)
Conflicts:	logrotate < 3.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# references symbols in the asterisk binary
%define		skip_post_check_so	libasteriskssl.so.*

%define _noautoprovfiles %{_libdir}/asterisk/modules/.*

%define _unpackaged_files_terminate_build 0

%description
Asterisk is an Open Source PBX and telephony development platform that
can both replace a conventional PBX and act as a platform for
developing custom telephony applications for delivering dynamic
content over a telephone similarly to how one can deliver dynamic
content through a web browser using CGI and a web server.

Asterisk talks to a variety of telephony hardware including BRI, PRI,
POTS, and IP telephony clients using the Inter-Asterisk eXchange
protocol (e.g. gnophone or miniphone). For more information and a
current list of supported hardware, see http://www.asterisk.org/.

%package devel
Summary:	Header files for Asterisk platform
Group:		Development

%description devel
Header files for Asterisk development platform.

%package utils
Summary:	Various utilities for Asterisk
Group:		Applications/Networking

%description utils
Various utilities built with Asterisk.

%package astman
Summary:	Astman - a text mode Manager for Asterisk
Group:		Applications/Networking

%description astman
Astman is a text mode Manager for Asterisk.

Astman connects to Asterisk by TCP, so you can run Astman on a
completely different computer than your Asterisk computer.


%package fax
Summary:	FAX applications for Asterisk
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description fax
FAX applications for Asterisk.

%package festival
Summary:	Festival application for Asterisk
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	festival

%description festival
Application for the Asterisk PBX that uses Festival to convert text to
speech.

%package gsm
Summary:	Support GSM audio encoding/decoding
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description gsm
Support GSM audio encoding/decoding.

%package http
Summary:	HTTP Server Support
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description http
HTTP Server Support.

%package ilbc
Summary:	iLBC codec for Asterisk
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description ilbc
Support iLBC audio encoding/decoding.

%package jabber
Summary:	Jabber/XMPP resources for Asterisk
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description jabber
Jabber/XMPP resources for Asterisk.



%package minivm
Summary:	MiniVM application for Asterisk
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description minivm
MiniVM application for Asterisk.

%package pjsip
Summary:	PJSIP Asterisk modules
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description pjsip
The chan_pjsip and res_pjsip* modules provided by this package provide
the new SIP driver for Asterisk, based on the PJSIP stack, to replace
the old, badly designed and quite buggy chan_sip module.

%package portaudio
Summary:	Module for Asterisk that uses the PortAudio library
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description portaudio
Module for Asterisk that uses the PortAudio library.

%package postgresql
Summary:	Applications for Asterisk that use PostgreSQL
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description postgresql
Applications for Asterisk that use PostgreSQL.

%package radius
Summary:	Applications for Asterisk that use RADIUS
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description radius
Applications for Asterisk that use RADIUS.

%package skinny
Summary:	Module for Asterisk that supportsthe SCCP/Skinny protocol
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description skinny
Module for Asterisk that supports the SCCP/Skinny protocol.

%package snmp
Summary:	Module that enables SNMP monitoring of Asterisk
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	mibs-dirs

%description snmp
Module that enables SNMP monitoring of Asterisk.

%package speex
Summary:	Speex codec support
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description speex
Speex codec support.

%package sqlite2
Summary:	SQLite 2 module for Asterisk
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description sqlite2
SQLite 2 module for Asterisk.

%package sqlite3
Summary:	SQLite 3 modules for Asterisk
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}
Obsoletes:	asterisk-sqlite < 12.0.0

%description sqlite3
SQLite 3 modules for Asterisk.

%package tds
Summary:	Modules for Asterisk that use FreeTDS
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description tds
Modules for Asterisk that use FreeTDS.

%package unistim
Summary:	Unistim channel for Asterisk
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description unistim
Unistim channel for Asterisk

%package voicemail
Summary:	Common Voicemail Modules for Asterisk
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	/usr/lib/sendmail
Requires:	sox

%description voicemail
Common Voicemail Modules for Asterisk.

%package vorbis
Summary:	Ogg Vorbis format support
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description vorbis
Ogg Vorbis format support.

# define apidocs as last package, as it is the biggest one
%package apidocs
Summary:	API documentation for Asterisk
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API documentation for Asterisk.

%prep
%setup 

# Fixup makefile so sound archives aren't downloaded/installed
%{__sed} -i -e 's/^all:.*$/all:/' sounds/Makefile
%{__sed} -i -e 's/^install:.*$/install:/' sounds/Makefile


%build
%{__aclocal} -I autoconf $(find third-party/ -maxdepth 1 -type d -printf "-I %p ")
%{__autoheader}
%{__autoconf}

export WGET="/bin/true"

# be sure to invoke ./configure with our flags
cd menuselect
%{__aclocal} -I ../autoconf
%{__autoheader}
%{__autoconf}
# we need just plain cli for building
%configure \
	--without-newt \
	--without-gtk2 \
	--without-curses \
	--without-ncurses
cd ..

%configure \
	%{__without oss SDL_image} \
	%{__without bluetooth bluetooth} \
	--without-gtk2 \
	--with-gnu-ld \
	--with-gsm=/usr \
	%{__without ilbc ilbc} \
	%{__without jack jack} \
	%{__without ldap ldap} \
	%{__without mysql mysqlclient} \
	%{__without oss oss} \
	%{__without pjsip pjproject} \
	%{__without portaudio portaudio} \
	%{__without pgsql postgres} \
	%{__without radius radius} \
	%{__without oss sdl} \
	%{__without tds tds} \
	%{__without odbc unixodbc}

test -e .cleancount || echo -n 1 > .cleancount
cp -f .cleancount .lastclean

%{__make} menuselect/menuselect
%{__make} menuselect-tree

cp %{SOURCE6} .
cp %{SOURCE7} .

menuselect/menuselect --disable res_corosync menuselect.makeopts
menuselect/menuselect --disable res_config_sqlite menuselect.makeopts
menuselect/menuselect --disable chan_oss menuselect.makeopts
menuselect/menuselect --disable cdr_tds --disable cel_tds menuselect.makeopts
menuselect/menuselect --disable codec_ilbc --disable format_ilbc menuselect.makeopts
menuselect/menuselect --disable res_config_ldap menuselect.makeopts
menuselect/menuselect --disable chan_mobile menuselect.makeopts
menuselect/menuselect --disable app_jack menuselect.makeopts
menuselect/menuselect --disable res_config_mysql --disable app_mysql --disable cdr_mysql menuselect.makeopts
menuselect/menuselect --disable res_config_pgsql --disable cdr_pgsql --disable cel_pgsql menuselect.makeopts
menuselect/menuselect --disable res_odbc --disable res_config_odbc --disable cdr_odbc --disable cdr_adaptive_odbc --disable cel_odbc menuselect.makeopts
menuselect/menuselect --disable cdr_radius --disable cel_radius menuselect.makeopts

%{__sed} -i -e 's/^MENUSELECT_OPTS_app_voicemail=.*$/MENUSELECT_OPTS_app_voicemail=FILE_STORAGE/' menuselect.makeopts

menuselect/menuselect --enable app_voicemail menuselect.makeopts

# workaround for build failing with asterisk-devel not installed
ln -s libasteriskssl.so.1 ./main/libasteriskssl.so

%{__make} DEBUG= \
	OPTIMIZE= \
	ASTVARRUNDIR=%{_localstatedir}/run/asterisk \
	ASTDATADIR=%{_datadir}/asterisk \
	ASTVARLIBDIR=%{_datadir}/asterisk \
	ASTDBDIR=%{_localstatedir}/spool/asterisk \
	%{?with_verbose:NOISY_BUILD=yes} \



%if %{with apidocs}
%{__make} progdocs \
	DEBUG= \
	OPTIMIZE= \
	ASTVARRUNDIR=%{_localstatedir}/run/asterisk \
	ASTDATADIR=%{_datadir}/asterisk \
	ASTVARLIBDIR=%{_datadir}/asterisk \
	ASTDBDIR=%{_localstatedir}/spool/asterisk \
	%{?with_verbose:NOISY_BUILD=yes} \
%endif

%install
rm -rf %{buildroot}
install -d %{buildroot}{/var/{log/asterisk/cdr-csv,spool/asterisk/monitor},/etc/{sysconfig,logrotate.d}} \
	%{buildroot}%{_mandir}/man1


%{__make} -j1 install \
	DEBUG= \
	OPTIMIZE= \
	DESTDIR=%{buildroot} \
	ASTVARRUNDIR=%{_localstatedir}/run/asterisk \
	ASTDATADIR=%{_datadir}/asterisk \
	ASTVARLIBDIR=%{_datadir}/asterisk \
	ASTDBDIR=%{_localstatedir}/spool/asterisk

%{__make} -j1 samples \
	DEBUG= \
	OPTIMIZE= \
	DESTDIR=%{buildroot} \
	ASTVARRUNDIR=%{_localstatedir}/run/asterisk \
	ASTDATADIR=%{_datadir}/asterisk \
	ASTVARLIBDIR=%{_datadir}/asterisk \
	ASTDBDIR=%{_localstatedir}/spool/asterisk


cp -a %{SOURCE2} %{buildroot}/etc/sysconfig/%{name}
cp -a %{SOURCE4} %{buildroot}/etc/logrotate.d/%{name}

# Systemd
mkdir -p %{buildroot}%{_unitdir}
install -m644 %{SOURCE5} %{buildroot}%{_unitdir}
rm -rf %{buildroot}%{_initrddir}

# systemd tmpfiles
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install %{SOURCE3} %{buildroot}/usr/lib/tmpfiles.d/%{name}.conf

# create some directories that need to be packaged
install -d %{buildroot}%{_datadir}/asterisk/moh
install -d %{buildroot}%{_datadir}/asterisk/sounds
ln -s %{_localstatedir}/lib/asterisk/licenses %{buildroot}%{_datadir}/asterisk/licenses

install -d %{buildroot}%{_localstatedir}/lib/asterisk/licenses
install -d %{buildroot}%{_localstatedir}/log/asterisk/cdr-custom
install -d %{buildroot}%{_localstatedir}/spool/asterisk/festival
install -d %{buildroot}%{_localstatedir}/spool/asterisk/monitor
install -d %{buildroot}%{_localstatedir}/spool/asterisk/outgoing
install -d %{buildroot}%{_localstatedir}/spool/asterisk/uploads

install utils/astman.1 %{buildroot}%{_mandir}/man1/astman.1

# Don't package the sample voicemail user
%{__rm} -r %{buildroot}%{_localstatedir}/spool/asterisk/voicemail/default

# Don't package example phone provision configs
%{__rm} -r %{buildroot}%{_datadir}/asterisk/phoneprov/*

# we're not using safe_asterisk
%{__rm} %{buildroot}%{_sbindir}/safe_asterisk
%{__rm} %{buildroot}%{_mandir}/man8/safe_asterisk.8*

%if %{with apidocs}
find doc/api -name '*.map' -size 0 -delete
%endif

# remove configuration files for components never built
%{__rm} %{buildroot}%{_sysconfdir}/asterisk/{app_skel,config_test,misdn,ooh323,test_sorcery,alsa,app_mysql,calendar,cdr_mysql,chan_dahdi,dbsep,hep,meetme,osp,pjproject,pjsip,pjsip_notify,pjsip_wizard,res_curl,res_pktccops,res_snmp,unistim}.conf

# remove configuration files for disabled optional components
%{__rm} %{buildroot}%{_sysconfdir}/asterisk/res_corosync.conf
%{__rm} %{buildroot}%{_sysconfdir}/asterisk/res_config_sqlite.conf
%{__rm} %{buildroot}%{_sysconfdir}/asterisk/oss.conf
%{__rm} %{buildroot}%{_sysconfdir}/asterisk/{cdr,cel}_tds.conf
%{__rm} %{buildroot}%{_sysconfdir}/asterisk/res_ldap.conf
%{__rm} %{buildroot}%{_sysconfdir}/asterisk/console.conf
%{__rm} %{buildroot}%{_sysconfdir}/asterisk/chan_mobile.conf
%{__rm} %{buildroot}%{_sysconfdir}/asterisk/res_config_mysql.conf
%{__rm} %{buildroot}%{_sysconfdir}/asterisk/{cdr,cel,res}_pgsql.conf
%{__rm} %{buildroot}%{_sysconfdir}/asterisk/{cdr{,_adaptive},cel,func,res}_odbc.conf
%{__rm} %{buildroot}%{_sysconfdir}/asterisk/extensions.lua

%{__rm} %{buildroot}%{_libdir}/asterisk/modules/app_page.so
%{__rm} %{buildroot}%{_libdir}/asterisk/modules/chan_unistim.so
%{__rm} %{buildroot}%{_libdir}/asterisk/modules/codec_lpc10.so
%{__rm} %{buildroot}%{_libdir}/asterisk/modules/codec_resample.so
%{__rm} %{buildroot}%{_libdir}/asterisk/modules/res_calendar.so
%{__rm} %{buildroot}%{_libdir}/asterisk/modules/res_calendar_caldav.so
%{__rm} %{buildroot}%{_libdir}/asterisk/modules/res_calendar_ews.so
%{__rm} %{buildroot}%{_libdir}/asterisk/modules/res_calendar_exchange.so
%{__rm} %{buildroot}%{_libdir}/asterisk/modules/res_calendar_icalendar.so
%{__rm} %{buildroot}%{_libdir}/asterisk/modules/res_format_attr_vp8.so
%{__rm} %{buildroot}%{_libdir}/asterisk/modules/res_hep.so
%{__rm} %{buildroot}%{_libdir}/asterisk/modules/res_hep_rtcp.so
%{__rm} %{buildroot}%{_libdir}/asterisk/modules/res_snmp.so

%{__rm} -f %{buildroot}%{_sbindir}/check_expr
%{__rm} -f %{buildroot}%{_sbindir}/check_expr2
%{__rm} %{buildroot}%{_sbindir}/rasterisk

%{__rm} -r %{buildroot}/usr/include/asterisk/doxygen

%clean
rm -rf %{buildroot}

%pre
/usr/bin/getent group asterisk || /usr/sbin/groupadd -g 188 asterisk
/usr/bin/getent passwd asterisk || /usr/sbin/useradd -g 188 -u 188 -r -d /var/lib/asterisk -s /sbin/nologin asterisk

%postun
if [ "$1" = 0 ]; then
	%userremove asterisk
	%groupremove asterisk
fi
%systemd_postun_with_restart %{name}.service

%post
/sbin/ldconfig
/sbin/chkconfig --add asterisk
# use -n (NOOP) as restart would be breaking all current calls.
%service -n asterisk restart "Asterisk daemon"
%systemd_post %{name}.service

%preun
if [ "$1" = "0" ]; then
	%service asterisk stop
	/sbin/chkconfig --del asterisk
fi
%systemd_preun %{name}.service

%triggerpostun -- %{name} < 1.6.1.12-0.1
# chown to asterisk previously root owned files
# loose one (not one that cames from rpm), as we're not trying to split the
# hair with file permission bits.
chown -R asterisk:asterisk /var/spool/asterisk
chown -R asterisk:asterisk /var/lib/asterisk

%triggerpostun -- %{name} < 12.0.0
%systemd_trigger %{name}.service

%files
%defattr(644,root,root,755)
%doc README *.txt ChangeLog BUGS CREDITS configs
%doc doc/asterisk.sgml

%attr(755,root,root) %{_sbindir}/astcanary
%attr(755,root,root) %{_sbindir}/astdb2bdb
%attr(755,root,root) %{_sbindir}/astdb2sqlite3
%attr(755,root,root) %{_sbindir}/asterisk
%attr(755,root,root) %{_sbindir}/astgenkey
%attr(755,root,root) %{_sbindir}/astversion
%attr(755,root,root) %{_sbindir}/autosupport
%{_mandir}/man8/astdb2bdb.8*
%{_mandir}/man8/astdb2sqlite3.8*
%{_mandir}/man8/asterisk.8*
%{_mandir}/man8/astgenkey.8*
%{_mandir}/man8/autosupport.8*

%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_unitdir}/%{name}.service

%attr(750,root,asterisk) %dir %{_sysconfdir}/asterisk
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/acl.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/adsi.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/agents.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/alarmreceiver.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/amd.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/ari.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/asterisk.adsi
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/asterisk.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/ccss.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/cdr.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/cdr_custom.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/cdr_manager.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/cdr_syslog.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/cel.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/cel_custom.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/cli.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/cli_aliases.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/cli_permissions.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/codecs.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/confbridge.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/dnsmgr.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/dsp.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/dundi.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/enum.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/extconfig.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/extensions.ael
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/extensions.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/features.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/followme.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/iax.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/iaxprov.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/indications.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/logger.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/manager.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/mgcp.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/modules.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/musiconhold.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/muted.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/phone.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/phoneprov.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/queuerules.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/queues.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/res_parking.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/res_stun_monitor.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/rtp.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/say.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/sip*.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/sla.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/smdi.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/sorcery.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/ss7.timers
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/stasis.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/statsd.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/telcordia-1.adsi
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/udptl.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/users.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/vpb.conf

%{_libdir}/libasteriskssl.so.1

%dir %{_libdir}/asterisk
%dir %{_libdir}/asterisk/modules

%attr(755,root,root) %{_libdir}/asterisk/modules/app_adsiprog.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_agent_pool.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_alarmreceiver.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_amd.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_authenticate.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_bridgewait.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_cdr.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_celgenuserevent.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_chanisavail.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_channelredirect.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_chanspy.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_confbridge.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_controlplayback.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_db.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_dial.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_dictate.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_directed_pickup.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_directory.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_disa.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_dumpchan.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_echo.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_exec.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_externalivr.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_followme.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_forkcdr.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_getcpeid.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_image.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_macro.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_milliwatt.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_mixmonitor.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_morsecode.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_mp3.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_nbscat.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_originate.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_playback.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_playtones.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_privacy.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_queue.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_read.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_readexten.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_record.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_saycounted.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_sayunixtime.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_senddtmf.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_sendtext.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_sms.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_softhangup.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_speech_utils.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_stack.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_stasis.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_system.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_talkdetect.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_test.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_transfer.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_url.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_userevent.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_verbose.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_waitforring.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_waitforsilence.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_waituntil.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_while.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_zapateller.so
%attr(755,root,root) %{_libdir}/asterisk/modules/bridge_builtin_features.so
%attr(755,root,root) %{_libdir}/asterisk/modules/bridge_builtin_interval_features.so
%attr(755,root,root) %{_libdir}/asterisk/modules/bridge_holding.so
%attr(755,root,root) %{_libdir}/asterisk/modules/bridge_native_rtp.so
%attr(755,root,root) %{_libdir}/asterisk/modules/bridge_simple.so
%attr(755,root,root) %{_libdir}/asterisk/modules/bridge_softmix.so
%attr(755,root,root) %{_libdir}/asterisk/modules/cdr_csv.so
%attr(755,root,root) %{_libdir}/asterisk/modules/cdr_custom.so
%attr(755,root,root) %{_libdir}/asterisk/modules/cdr_manager.so
%attr(755,root,root) %{_libdir}/asterisk/modules/cdr_syslog.so
%attr(755,root,root) %{_libdir}/asterisk/modules/cel_custom.so
%attr(755,root,root) %{_libdir}/asterisk/modules/cel_manager.so
%attr(755,root,root) %{_libdir}/asterisk/modules/chan_bridge_media.so
%attr(755,root,root) %{_libdir}/asterisk/modules/chan_iax2.so
%attr(755,root,root) %{_libdir}/asterisk/modules/chan_mgcp.so
%attr(755,root,root) %{_libdir}/asterisk/modules/chan_phone.so
%attr(755,root,root) %{_libdir}/asterisk/modules/chan_rtp.so
%attr(755,root,root) %{_libdir}/asterisk/modules/chan_sip.so
%attr(755,root,root) %{_libdir}/asterisk/modules/codec_a_mu.so
%attr(755,root,root) %{_libdir}/asterisk/modules/codec_adpcm.so
%attr(755,root,root) %{_libdir}/asterisk/modules/codec_alaw.so
%attr(755,root,root) %{_libdir}/asterisk/modules/codec_g722.so
%attr(755,root,root) %{_libdir}/asterisk/modules/codec_g726.so
%attr(755,root,root) %{_libdir}/asterisk/modules/codec_ulaw.so
%attr(755,root,root) %{_libdir}/asterisk/modules/format_g719.so
%attr(755,root,root) %{_libdir}/asterisk/modules/format_g723.so
%attr(755,root,root) %{_libdir}/asterisk/modules/format_g726.so
%attr(755,root,root) %{_libdir}/asterisk/modules/format_g729.so
%attr(755,root,root) %{_libdir}/asterisk/modules/format_h263.so
%attr(755,root,root) %{_libdir}/asterisk/modules/format_h264.so
%attr(755,root,root) %{_libdir}/asterisk/modules/format_jpeg.so
%attr(755,root,root) %{_libdir}/asterisk/modules/format_pcm.so
%attr(755,root,root) %{_libdir}/asterisk/modules/format_siren14.so
%attr(755,root,root) %{_libdir}/asterisk/modules/format_siren7.so
%attr(755,root,root) %{_libdir}/asterisk/modules/format_sln.so
%attr(755,root,root) %{_libdir}/asterisk/modules/format_vox.so
%attr(755,root,root) %{_libdir}/asterisk/modules/format_wav.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_aes.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_audiohookinherit.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_base64.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_blacklist.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_callcompletion.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_callerid.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_cdr.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_channel.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_config.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_cut.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_db.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_devstate.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_dialgroup.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_dialplan.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_enum.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_env.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_extstate.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_frame_trace.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_global.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_groupcount.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_hangupcause.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_holdintercept.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_iconv.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_jitterbuffer.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_lock.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_logic.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_math.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_md5.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_module.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_periodic_hook.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_pitchshift.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_presencestate.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_rand.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_realtime.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_sha1.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_shell.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_sorcery.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_sprintf.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_srv.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_strings.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_sysinfo.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_talkdetect.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_timeout.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_uri.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_version.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_volume.so
%attr(755,root,root) %{_libdir}/asterisk/modules/pbx_ael.so
%attr(755,root,root) %{_libdir}/asterisk/modules/pbx_config.so
%attr(755,root,root) %{_libdir}/asterisk/modules/pbx_dundi.so
%attr(755,root,root) %{_libdir}/asterisk/modules/pbx_loopback.so
%attr(755,root,root) %{_libdir}/asterisk/modules/pbx_realtime.so
%attr(755,root,root) %{_libdir}/asterisk/modules/pbx_spool.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_adsi.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_ael_share.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_agi.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_ari.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_ari_applications.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_ari_asterisk.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_ari_bridges.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_ari_channels.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_ari_device_states.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_ari_endpoints.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_ari_events.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_ari_model.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_ari_playbacks.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_ari_recordings.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_ari_sounds.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_clialiases.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_clioriginate.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_convert.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_crypto.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_endpoint_stats.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_format_attr_celt.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_format_attr_h263.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_format_attr_h264.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_format_attr_opus.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_format_attr_silk.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_http_websocket.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_limit.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_manager_devicestate.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_manager_presencestate.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_monitor.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_mutestream.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_musiconhold.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_parking.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_phoneprov.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_realtime.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_rtp_asterisk.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_rtp_multicast.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_security_log.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_smdi.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_sorcery_astdb.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_sorcery_config.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_sorcery_memory.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_sorcery_memory_cache.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_sorcery_realtime.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_speech.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_srtp.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_stasis.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_stasis_answer.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_stasis_device_state.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_stasis_playback.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_stasis_recording.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_stasis_snoop.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_stun_monitor.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_timing_pthread.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_timing_timerfd.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_statsd.so
#systemd tmpfiles
%attr(644,root,root) /usr/lib/tmpfiles.d/%{name}.conf

%dir %{_datadir}/asterisk
%dir %{_datadir}/asterisk/agi-bin
%dir %{_datadir}/asterisk/firmware
%dir %{_datadir}/asterisk/firmware/iax
%dir %{_datadir}/asterisk/images
%dir %{_datadir}/asterisk/moh
%dir %{_datadir}/asterisk/sounds
%dir %attr(750,root,asterisk) %{_datadir}/asterisk/keys
# no need to protect publicly downloaded and packaged .pub
#%{_datadir}/asterisk/keys/*.pub
%{_datadir}/asterisk/images/*.jpg
%{_datadir}/asterisk/phoneprov
%{_datadir}/asterisk/licenses

%dir %{_datadir}/asterisk/documentation
%{_datadir}/asterisk/documentation/appdocsxml.dtd
%{_datadir}/asterisk/documentation/appdocsxml.xslt
%{_datadir}/asterisk/documentation/core-en_US.xml

%dir %{_datadir}/asterisk/rest-api
%{_datadir}/asterisk/rest-api/*.json

%attr(770,root,asterisk) %dir %{_localstatedir}/lib/asterisk
%dir %attr(750,root,asterisk) %{_localstatedir}/lib/asterisk/licenses

%attr(770,root,asterisk) %dir %{_localstatedir}/log/asterisk
%attr(770,root,asterisk) %dir %{_localstatedir}/log/asterisk/cdr-csv
%attr(770,root,asterisk) %dir %{_localstatedir}/log/asterisk/cdr-custom

%attr(770,root,asterisk) %dir %{_localstatedir}/spool/asterisk
%attr(770,root,asterisk) %dir %{_localstatedir}/spool/asterisk/monitor
%attr(770,root,asterisk) %dir %{_localstatedir}/spool/asterisk/outgoing
%attr(770,root,asterisk) %dir %{_localstatedir}/spool/asterisk/tmp
%attr(770,root,asterisk) %dir %{_localstatedir}/spool/asterisk/uploads
%attr(770,root,asterisk) %dir %{_localstatedir}/spool/asterisk/voicemail

%attr(775,root,asterisk) %dir %{_localstatedir}/run/asterisk

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/asterisk
%{_includedir}/asterisk/*.h
%{_includedir}/asterisk.h

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc doc/api/*
%endif

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/aelparse
%attr(755,root,root) %{_sbindir}/conf2ael
%attr(755,root,root) %{_sbindir}/muted
%attr(755,root,root) %{_sbindir}/stereorize
%attr(755,root,root) %{_sbindir}/streamplayer

%files astman
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/astman
%{_mandir}/man1/astman.1*

%files fax
%defattr(644,root,root,755)
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/res_fax.conf
%attr(755,root,root) %{_libdir}/asterisk/modules/res_fax.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_fax_spandsp.so

%files festival
%defattr(644,root,root,755)
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/festival.conf
%attr(770,root,asterisk) %dir %{_localstatedir}/spool/asterisk/festival
%attr(755,root,root) %{_libdir}/asterisk/modules/app_festival.so

%files gsm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/asterisk/modules/codec_gsm.so
%attr(755,root,root) %{_libdir}/asterisk/modules/format_gsm.so
%attr(755,root,root) %{_libdir}/asterisk/modules/format_wav_gsm.so

%files http
%defattr(644,root,root,755)
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/http.conf
%attr(755,root,root) %{_libdir}/asterisk/modules/res_http_post.so
%{_datadir}/asterisk/static-http

%if %{with ilbc}
%files ilbc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/asterisk/modules/codec_ilbc.so
%attr(755,root,root) %{_libdir}/asterisk/modules/format_ilbc.so
%endif

%files jabber
%defattr(644,root,root,755)
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/motif.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/xmpp.conf
%attr(755,root,root) %{_libdir}/asterisk/modules/chan_motif.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_xmpp.so


%files minivm
%defattr(644,root,root,755)
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/extensions_minivm.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/minivm.conf
%attr(755,root,root) %{_libdir}/asterisk/modules/app_minivm.so

%if %{with pjsip}
%files pjsip
%defattr(644,root,root,755)
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/pjproject.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/pjsip.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/pjsip_notify.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/pjsip_wizard.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/hep.conf
%attr(755,root,root) %{_libdir}/asterisk/modules/chan_pjsip.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_pjsip_aor.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_pjsip_contact.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_pjsip_endpoint.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_hep.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_hep_pjsip.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_hep_rtcp.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjproject.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_acl.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_authenticator_digest.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_caller_id.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_config_wizard.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_dialog_info_body_generator.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_diversion.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_dlg_options.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_dtmf_info.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_empty_info.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_endpoint_identifier_anonymous.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_endpoint_identifier_ip.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_endpoint_identifier_user.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_exten_state.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_header_funcs.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_history.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_logger.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_messaging.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_multihomed.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_mwi_body_generator.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_mwi.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_nat.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_notify.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_one_touch_record_info.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_outbound_authenticator_digest.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_outbound_publish.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_outbound_registration.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_path.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_phoneprov_provider.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_pidf_body_generator.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_pidf_digium_body_supplement.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_pidf_eyebeam_body_supplement.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_publish_asterisk.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_pubsub.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_refer.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_registrar_expire.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_registrar.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_rfc3326.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_sdp_rtp.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_send_to_voicemail.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_session.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_sips_contact.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_t38.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_transport_management.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_transport_websocket.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_pjsip_xpidf_body_generator.so
%endif


%files skinny
%defattr(644,root,root,755)
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/skinny.conf
%attr(755,root,root) %{_libdir}/asterisk/modules/chan_skinny.so

%files speex
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/asterisk/modules/codec_speex.so
%attr(755,root,root) %{_libdir}/asterisk/modules/func_speex.so

%if %{with sqlite2}
%files sqlite2
%defattr(644,root,root,755)
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/res_config_sqlite.conf
%attr(755,root,root) %{_libdir}/asterisk/modules/res_config_sqlite.so
%endif

%files sqlite3
%defattr(644,root,root,755)
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/cdr_sqlite3_custom.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/cel_sqlite3_custom.conf
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/res_config_sqlite3.conf
%attr(755,root,root) %{_libdir}/asterisk/modules/cdr_sqlite3_custom.so
%attr(755,root,root) %{_libdir}/asterisk/modules/cel_sqlite3_custom.so
%attr(755,root,root) %{_libdir}/asterisk/modules/res_config_sqlite3.so

%files voicemail
%defattr(644,root,root,755)
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/voicemail.conf
%attr(755,root,root) %{_libdir}/asterisk/modules/func_vmcount.so
%attr(755,root,root) %{_libdir}/asterisk/modules/app_voicemail.so


%files vorbis
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/asterisk/modules/format_ogg_vorbis.so
