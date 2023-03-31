Name:		texlive-stix2-otf
Version:	58735
Release:	2
Summary:	OpenType Unicode text and maths fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/stix2-otf
License:	ofl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stix2-otf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stix2-otf.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Scientific and Technical Information eXchange (STIX) fonts
are intended to satisfy the demanding needs of authors,
publishers, printers, and others working in the scientific,
medical, and technical fields. They combine a comprehensive
Unicode-based collection of mathematical symbols and alphabets
with a set of text faces suitable for professional publishing.
The fonts are available royalty-free under the SIL Open Font
License.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/fonts/opentype/public/stix2-otf
%doc %{_texmfdistdir}/doc/fonts/stix2-otf

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
