# revision 17224
# category Package
# catalog-ctan /macros/latex/contrib/bbm
# catalog-date 2010-02-15 23:28:51 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-bbm-macros
Version:	20180303
Release:	2
Summary:	LaTeX support for "blackboard-style" cm fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bbm
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bbm-macros.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bbm-macros.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bbm-macros.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100215-2
+ Revision: 749507
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100215-1
+ Revision: 717890
- texlive-bbm-macros
- texlive-bbm-macros
- texlive-bbm-macros
- texlive-bbm-macros
- texlive-bbm-macros

