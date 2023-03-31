Name:		texlive-pgf-periodictable
Version:	64974
Release:	2
Summary:	Create custom periodic tables of elements
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pgf-periodictable
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-periodictable.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-periodictable.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The purpose of this package is to provide the Periodic Table of
Elements in a simple way. It relies on PGF/TikZ to offer a full
or partial periodic table with a variety of options and
displaying the desired data for all the 118 elements. It can be
done in six languages: English, French, German, Portuguese
(from Portugal and from Brazil), Spanish and Italian.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/pgf-periodictable
%doc %{_texmfdistdir}/doc/latex/pgf-periodictable

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
