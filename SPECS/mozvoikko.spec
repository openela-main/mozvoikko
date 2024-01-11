%global moz_ext_dir %{_datadir}/mozilla/extensions

%global firefox_app_id \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}
%global src_ext_id \{b676e3ff-cda7-4e0c-b2b8-74e4bb40a67a\}
%global inst_dir %{moz_ext_dir}/%{firefox_app_id}/%{src_ext_id}

%global thunderbird_app_id \{3550f703-e582-4d05-9a08-453d09bdfdc6\}
%global thunderbird_inst_dir %{moz_ext_dir}/%{thunderbird_app_id}/%{src_ext_id}

Name:           mozvoikko
Version:        2.1
Release:        5%{?dist}
Summary:        Finnish Voikko spell-checker extension for Mozilla programs
Group:          Applications/Internet
License:        GPLv2+
URL:            http://voikko.sourceforge.net
# Usual format of test release URLs
#Source0:        http://www.puimula.org/htp/testing/%{name}-%{version}rc1.tar.gz
# Usual format of stable release URLs
Source0:        http://www.puimula.org/voikko-sources/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch
# Owns the needed directories
Requires:       mozilla-filesystem
# Require the spell-checking library
Requires:       libvoikko
# Obsolete the old arch-specific 1.9 series
Obsoletes:      %{name} < 1.9.0-100
# Provide a langpack so we can be automatically installed when necessary
Provides:       firefox-langpack-fi

%description
This is mozvoikko, an extension for Mozilla programs for using the Finnish
spell-checker Voikko.

%prep
%setup -q

%install
rm -rf %{buildroot}
sed -i "s|<em:maxVersion>[^<]*</em:maxVersion>|<em:maxVersion>*</em:maxVersion>|g" install.rdf
install -dm 755 \
    %{buildroot}%{inst_dir}/components
install -pm 644 components/MozVoikko2.js \
    %{buildroot}%{inst_dir}/components/MozVoikko2.js
install -pm 644 chrome.manifest \
    %{buildroot}%{inst_dir}/chrome.manifest
install -pm 644 install.rdf \
    %{buildroot}%{inst_dir}/install.rdf

# Symlink from the Thunderbird extension to the Firefox extension
mkdir -p %{buildroot}%{moz_ext_dir}/%{thunderbird_app_id}
ln -s %{inst_dir} %{buildroot}%{thunderbird_inst_dir}

%files
%defattr(-,root,root,-)
%doc ChangeLog COPYING README
%{inst_dir}
%{thunderbird_inst_dir}

%changelog
* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Nov 01 2014 Ville-Pekka Vainio <vpvainio AT iki.fi> - 2.1-1
- New upstream release.
- Update upstream URLs.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 24 2012 Bill Nottingham <notting@redhat.com> - 2.0.1-3
- provide firefox-langpack-fi for use with yum-langpacks

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 06 2012 Ville-Pekka Vainio <vpvainio AT iki.fi> - 2.0.1-1
- New upstream release.
- This release fixes a bug that prevented changing spell checking language to
  anything else than Finnish in Firefox 9.
- Better sed replace for maxVersion in install.rdf.

* Mon Dec 26 2011 Ville-Pekka Vainio <vpvainio AT iki.fi> - 2.0-3
- Change maxVersion to * in install.rdf so that the extension package does not
  have to be updated with every Xulrunner update if it works otherwise.

* Sat Nov 05 2011 Ville-Pekka Vainio <vpvainio AT iki.fi> - 2.0-2
- Use the same macros as the mozilla-adblockplus package
- Add support for Thunderbird by symlinking the extension from Firefox

* Sun Oct 30 2011 Ville-Pekka Vainio <vpvainio AT iki.fi> - 2.0-1
- Package the noarch JavaScript version of the extension, obsolete the old
  arch-specific 1.9 versions.

* Mon Oct 03 2011 Jan Horak <jhorak@redhat.com> - 1.9.0-9
- Rebuild against newer gecko

* Tue Sep 27 2011 Jan Horak <jhorak@redhat.com> - 1.9.0-8
- Rebuild against newer gecko

* Tue Sep 06 2011 Jan Horak <jhorak@redhat.com> - 1.9.0-7
- Rebuild against newer gecko

* Wed Aug 17 2011 Jan Horak <jhorak@redhat.com> - 1.9.0-6
- Rebuild against newer gecko

* Wed Jun 22 2011 Jan Horak <jhorak@redhat.com> - 1.9.0-5
- Rebuild against newer gecko

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 14 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 1.9.0-3
- Upstream finally released a 1.9.0 tarball, switch to it
- Drop integrated (with improvements) SYSTEM_LIBVOIKKO patch

* Thu Dec 09 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 1.9.0-2
- Add a patch to fix compilation of mozVoikkoUtils.cpp when SYSTEM_LIBVOIKKO is
  defined
- Remove the xpidl call, nsIMozvoikkoHelper.h is not needed after applying the
  patch

* Wed Dec 08 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 1.9.0-1
- Update to 1.9.0 to fix FTBFS bug #660944
- Add a patch from the upstream mailing list to fix xulrunner includes and
  linking
- Generate the nsIMozvoikkoHelper.h file with xpidl
- Remove unneeded BuildRoot and the clean section

* Wed Jun 23 2010 Jan Horak <jhorak@redhat.com> - 1.0-11
- Rebuild against newer gecko

* Mon Apr 12 2010 Martin Stransky <stransky@redhat.com> - 1.0-10
- Updated gecko dependency

* Sat Apr 03 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 1.0-9
- Rebuild against newer gecko

* Tue Mar 23 2010 Jan Horak <jhorak@redhat.com> - 1.0-8
- Rebuild against newer gecko

* Wed Nov 25 2009 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 1.0-7
- Rebuild against newer gecko

* Thu Nov 05 2009 Jan Horak <jhorak@redhat.com> - 1.0-6
- Rebuild against newer gecko

* Tue Oct 27 2009 Jan Horak <jhorak@redhat.com> - 1.0-5
- Rebuild against newer gecko

* Tue Sep 15 2009 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 1.0-4
- Drop Requires for libmalaga, the current version of libvoikko in Fedora
  Rawhide doesn't depend on libmalaga anymore

* Fri Sep 11 2009 Jan Horak <jhorak@redhat.com> - 1.0-3
- Rebuild against newer gecko

* Sun Sep 06 2009 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 1.0-2
- Use global instead of define, except in gecko_ver as that might be used
  in the xulrunner rebuild scripts.

* Mon Aug 10 2009 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 1.0-1
- Update to 1.0.
- Use "official" upstream source, the RC sources have been removed. 
- This is mostly a cosmetic change, no code was changed, only the XML file
  defining the extension version.

* Thu Aug 06 2009 Jan Horak <jhorak@redhat.com> - 0.9.7-0.8.rc1
- Rebuild against newer gecko

* Tue Aug 04 2009 Jan Horak <jhorak@redhat.com> - 0.9.7-0.7.rc1
- Rebuild against newer gecko

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-0.6.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jul 19 2009 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 0.9.7-0.5.rc1
- Rebuild against newer gecko
- Bump Release to fix upgrade path

* Mon Apr 27 2009 Christopher Aillon <caillon@redhat.com> - 0.9.7-0.3.rc1
- Rebuild against newer gecko

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 0.9.7-0.1.rc1
- New RC
  - The unstable nsIXULRuntime interface is not used anymore

* Tue Feb 17 2009 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 0.9.6-0.1.rc2
- New RC
- All patches applied upstream, some documentation updates

* Tue Jan 27 2009 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 0.9.5-6
- Add a series of patches developed together with upstream and the
  Ubuntu/Debian maintainer: 
  - Uses pkg-config --cflags and --libs, no rpath anymore
  - Cleans up some unneeded cruft from Makefile.xulrunner
  - Uses -Wl,--as-needed to reduce shared library dependencies
  - Some discussion about pkg-config and rpath in Launchpad #297169

* Fri Dec 26 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 0.9.5-5
- Rebuild against gecko 1.9.1
- Bump Release so that it's at least as high as in F10 and F9

* Mon Sep 29 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 0.9.5-3
- Rebuild against newer gecko

* Sat Aug 30 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 0.9.5-2
- Fix the xulrunner requires:
  - Add define gecko_ver 1.9.0.1
  - Add Requires: gecko-libs = gecko_ver
  - Add BuildRequires: gecko-devel-unstable = gecko_ver
  - Remove all actual xulrunner requires
- Redo the Makefile.xulrunner includes patch, we only need the stable and
  unstable header dirs in Fedora

* Thu Jul 24 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 0.9.5-1
- Bump Release for initial Fedora build

* Fri Jul 18 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 0.9.5-0.2
- Add patch to remove xulrunner unstable include from Makefile.xulrunner
  and only BuildRequire xulrunner-devel, not xulrunner-devel-unstable
- Change Group to Applications/Internet
- Add dependency to the sonames libvoikko.so.1 and libmalaga.so.7

* Mon Jun 24 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 0.9.5-0.1
- New upstream release

* Mon May 31 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 0.9.4.1.3-0.1
- New upstream release, the Makefile.xulrunner path patch is no longer needed

* Mon May 26 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 0.9.4.1.2-0.1
- New upstream release, Makefile.xulrunner paths are no longer hardcoded,
  VOIKKO_INCLUDES is dropped completely
- Path patch updated, most notably include directories, even though the build
  worked even before for some reason

* Mon May 26 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 0.9.4.1.1-0.3
- Change name to mozvoikko to reflect the possibility of this package later
  supporting Thunderbird and Seamonkey as well
- Change summary and description accordingly
- Add firefox to Requires, because currently it's the only program which can
  use mozvoikko
- Drop BR xulrunner-devel, the -unstable package is enough to require for now

* Sat May 24 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 0.9.4.1.1-0.1
- New upstream release
- Use the new extension-files and install-unpacked make targets
- Path patch edited accordingly

* Fri May 23 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 0.9.4.1-0.1
- Initial package

