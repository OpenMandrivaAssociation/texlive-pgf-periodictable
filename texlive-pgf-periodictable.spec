%global tl_name pgf-periodictable
%global tl_revision 78931

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1.6a
Release:	%{tl_revision}.1
Summary:	Create custom periodic tables of elements
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/pgf-periodictable
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-periodictable.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-periodictable.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The purpose of this package is to provide the Periodic Table of Elements
in a simple way. It relies on PGF/TikZ to offer a full or partial
periodic table with a variety of options and displaying the desired data
for all the 118 elements. It can be done in different languages:
English, French, German, Portuguese (from Portugal and from Brazil),
Spanish, Italian and translations provided by user contributions --
currently in Dutch, Chinese, Russian, Ukrainian and Slovenian.
Compatible with pdfLaTeX, LuaLaTeX and XeLaTeX engines.

