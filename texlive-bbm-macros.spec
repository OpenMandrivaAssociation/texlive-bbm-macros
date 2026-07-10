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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides LaTeX support for Blackboard variants of Computer Modern fonts.
Declares a font family bbm so you can in principle write running text in
blackboard bold, and lots of math alphabets for using the fonts within
maths.

