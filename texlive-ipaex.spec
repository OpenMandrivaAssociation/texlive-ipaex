# revision 24458
# category Package
# catalog-ctan /fonts/ipaex
# catalog-date 2011-11-02 12:24:01 +0100
# catalog-license other-free
# catalog-version undef
Name:		texlive-ipaex
Version:	20111102
Release:	1
Summary:	IPA and IPAex fonts from Information-technology Promotion Agency, Japan
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/ipaex
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ipaex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ipaex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The fonts provide fixed-width glyphs for Kana and Kanji
characters, proportional width glyphs for Western characters.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvipdfmx/ipaex/otf-ipa.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ipaex/otf-ipaex.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ipaex/ptex-ipa.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ipaex/ptex-ipaex.map
%{_texmfdistdir}/fonts/truetype/public/ipaex/ipaexg.ttf
%{_texmfdistdir}/fonts/truetype/public/ipaex/ipaexm.ttf
%{_texmfdistdir}/fonts/truetype/public/ipaex/ipag.ttf
%{_texmfdistdir}/fonts/truetype/public/ipaex/ipam.ttf
%doc %{_texmfdistdir}/doc/fonts/ipaex/Copyright
%doc %{_texmfdistdir}/doc/fonts/ipaex/README
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
