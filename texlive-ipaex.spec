Name:		texlive-ipaex
Version:	20180303
Release:	2
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
%{_texmfdistdir}/fonts/truetype/public/ipaex
%doc %{_texmfdistdir}/doc/fonts/ipaex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
