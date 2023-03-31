Name:		texlive-bbm-macros
Version:	17224
Release:	2
Summary:	LaTeX support for "blackboard-style" cm fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bbm
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bbm-macros.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bbm-macros.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bbm-macros.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides LaTeX support for Blackboard variants of Computer
Modern fonts. Declares a font family bbm so you can in
principle write running text in blackboard bold, and lots of
math alphabets for using the fonts within maths.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bbm-macros/bbm.sty
%{_texmfdistdir}/tex/latex/bbm-macros/ubbm.fd
%{_texmfdistdir}/tex/latex/bbm-macros/ubbmss.fd
%{_texmfdistdir}/tex/latex/bbm-macros/ubbmtt.fd
%doc %{_texmfdistdir}/doc/latex/bbm-macros/README
%doc %{_texmfdistdir}/doc/latex/bbm-macros/bbm.pdf
#- source
%doc %{_texmfdistdir}/source/latex/bbm-macros/bbm.drv
%doc %{_texmfdistdir}/source/latex/bbm-macros/bbm.dtx
%doc %{_texmfdistdir}/source/latex/bbm-macros/bbm.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
