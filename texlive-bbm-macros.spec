%global tl_name bbm-macros
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	LaTeX support for blackboard-style cm fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bbm
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bbm-macros.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bbm-macros.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bbm-macros.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides LaTeX support for Blackboard variants of Computer Modern fonts.
Declares a font family bbm so you can in principle write running text in
blackboard bold, and lots of math alphabets for using the fonts within
maths.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bbm-macros
%dir %{_datadir}/texmf-dist/source/latex/bbm-macros
%dir %{_datadir}/texmf-dist/tex/latex/bbm-macros
%doc %{_datadir}/texmf-dist/doc/latex/bbm-macros/README
%doc %{_datadir}/texmf-dist/doc/latex/bbm-macros/bbm.pdf
%doc %{_datadir}/texmf-dist/source/latex/bbm-macros/bbm.drv
%doc %{_datadir}/texmf-dist/source/latex/bbm-macros/bbm.dtx
%doc %{_datadir}/texmf-dist/source/latex/bbm-macros/bbm.ins
%{_datadir}/texmf-dist/tex/latex/bbm-macros/bbm.sty
%{_datadir}/texmf-dist/tex/latex/bbm-macros/ubbm.fd
%{_datadir}/texmf-dist/tex/latex/bbm-macros/ubbmss.fd
%{_datadir}/texmf-dist/tex/latex/bbm-macros/ubbmtt.fd
