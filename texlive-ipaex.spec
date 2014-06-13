# revision 29849
# category Package
# catalog-ctan /fonts/ipaex
# catalog-date 2011-11-03 09:19:42 +0100
# catalog-license other-free
# catalog-version undef
Name:		texlive-ipaex
Version:	20111103
Release:	10
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

%description
The fonts provide fixed-width glyphs for Kana and Kanji
characters, proportional width glyphs for Western characters.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/truetype/public/ipaex/ipaexg.ttf
%{_texmfdistdir}/fonts/truetype/public/ipaex/ipaexm.ttf
%{_texmfdistdir}/fonts/truetype/public/ipaex/ipag.ttf
%{_texmfdistdir}/fonts/truetype/public/ipaex/ipam.ttf
%doc %{_texmfdistdir}/doc/fonts/ipaex/Copyright
%doc %{_texmfdistdir}/doc/fonts/ipaex/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
