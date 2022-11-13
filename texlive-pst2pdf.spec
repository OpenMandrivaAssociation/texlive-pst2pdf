Name:		texlive-pst2pdf
Version:	56172
Release:	1
Summary:	A script to compile pstricks documents via pdftex
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/scripts/pst2pdf
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst2pdf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst2pdf.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-pst2pdf.bin = %{EVRD}

%description
The script extracts the preamble of the document and runs all
\begin{postscript}...\end{postscript}
\begin{pspicture}...\end{pspicture} and
\pspicture...\endpspicture separately through LaTeX with the
same preamble as the original document; thus it creates EPS,
PNG and PDF files of these snippets. In a final PDFLaTeX run
the script replaces the environments with \includegraphics to
include the processed snippets. Detail documentation is
acquired from the document itself via Perldoc.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/pst2pdf
%{_texmfdistdir}/scripts/pst2pdf
%doc %{_texmfdistdir}/doc/support/pst2pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/pst2pdf/pst2pdf.pl pst2pdf
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
