Summary: GNOME Applications panel grouping applet
Name: quick-lounge-applet
Version: 2.12.5
Release: %mkrel 1
License: GPL
Group: Graphical desktop/GNOME
URL: http://quick-lounge.sourceforge.net/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libpanel-applet-devel
BuildRequires: gnome-menus-devel >= 2.12.0
BuildRequires: gnome-desktop-devel
BuildRequires: perl-XML-Parser
BuildRequires: scrollkeeper
Requires(post):		scrollkeeper >= 0.3
Requires(postun):		scrollkeeper >= 0.3

%description
The Quick Lounge applet is an applet for the GNOME Panel.
With this applet you can organize your preferred applications 
in a single place. You can add spaces between applications, they 
can be used to group together applications with similar tasks.

When the applet size exceeds the available space a menu containing the 
remaing launchers is created. The menu can be accessed pressing the arrow 
button located at the end of the applet. The menu displays spaces 
as separators.

%prep
%setup -q

%build

%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%makeinstall_std

%find_lang %{name} --with-gnome
%find_lang quick-lounge --with-gnome
cat quick-lounge.lang >> %name.lang
for omf in %buildroot%_datadir/omf/*/{*-??.omf,*-??_??.omf};do
echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed s!%buildroot!!)" >> %name.lang
done

# remove unpackaged files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.{la,a}
rm -rf %buildroot/var



%clean
rm -rf $RPM_BUILD_ROOT

%post
%post_install_gconf_schemas quick-lounge
%update_scrollkeeper
%update_icon_cache hicolor

%preun
%preun_uninstall_gconf_schemas quick-lounge

%postun
%clean_scrollkeeper
%clean_icon_cache hicolor


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc NEWS AUTHORS ChangeLog
%{_sysconfdir}/gconf/schemas/quick-lounge.schemas
%{_libexecdir}/%name
%{_libdir}/bonobo/servers/*
%{_datadir}/gnome-2.0/ui/*
%dir %_datadir/omf/%name
%_datadir/omf/%name/quick-lounge-C.omf
%_datadir/%name
%_datadir/icons/hicolor/*/apps/%name.png


