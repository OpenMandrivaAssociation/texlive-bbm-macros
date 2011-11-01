Name:		texlive-bbm-macros
Version:	20100215
Release:	1
Summary:	LaTeX support for "blackboard-style" cm fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bbm
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bbm-macros.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bbm-macros.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bbm-macros.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Provides LaTeX support for Blackboard variants of Computer
Modern fonts. Declares a font family bbm so you can in
principle write running text in blackboard bold, and lots of
math alphabets for using the fonts within maths.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
