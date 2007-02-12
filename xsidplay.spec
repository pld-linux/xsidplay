Summary:	SID music player for X11
Summary(pl.UTF-8):   Odtwarzacz muzyki SID dla X11
Name:		xsidplay
Version:	1.6.5.2
Release:	1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://www.geocities.com/siliconvalley/lakes/5147/sidplay/packages/%{name}-%{version}.tgz
# Source0-md5:	68669cf99904a7384a65ded5fcdd3c97
Patch0:		%{name}-desktop.patch
URL:		http://www.geocities.com/SiliconValley/Lakes/5147/sidplay/linux.html
BuildRequires:	autoconf
BuildRequires:	libsidplay-devel >= 1.36.52
BuildRequires:	libstdc++-devel
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a graphical frontend to the SIDPLAY library - Commodore 64
music player and SID chip emulator.

%description -l pl.UTF-8
Graficzna nakładka do biblioteki SIDPLAY - odtwarzacza muzyki z
Commodore 64 i emulatora układu dźwiękowego SID.

%prep
%setup -q
%patch0 -p0

%build
%{__autoconf}
%configure \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}
install xsidplay.desktop $RPM_BUILD_ROOT%{_desktopdir}
install xsidplay.xpm $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README* STIL.faq hv_sids.faq
%attr(755,root,root) %{_bindir}/*
%{_datadir}/xsidplay
%{_desktopdir}/xsidplay.desktop
%{_mandir}/man1/*
%{_pixmapsdir}/xsidplay.xpm
