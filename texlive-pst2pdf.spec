# revision 31118
# category Package
# catalog-ctan /graphics/pstricks/scripts/pst2pdf
# catalog-date 2013-07-06 19:43:54 +0200
# catalog-license gpl
# catalog-version 0.15
Name:		texlive-pst2pdf
Version:	0.15
Release:	7
Summary:	A script to compile pstricks documents via pdftex
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/scripts/pst2pdf
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst2pdf.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst2pdf.doc.tar.xz
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
%{_texmfdistdir}/scripts/pst2pdf/pst2pdf.pl
%doc %{_texmfdistdir}/doc/latex/pst2pdf/Changes
%doc %{_texmfdistdir}/doc/latex/pst2pdf/Makefile.doc
%doc %{_texmfdistdir}/doc/latex/pst2pdf/README
%doc %{_texmfdistdir}/doc/latex/pst2pdf/pst2pdf-doc.bib
%doc %{_texmfdistdir}/doc/latex/pst2pdf/pst2pdf-doc.pdf
%doc %{_texmfdistdir}/doc/latex/pst2pdf/pst2pdf-doc.tex
%doc %{_texmfdistdir}/doc/latex/pst2pdf/test.pdf
%doc %{_texmfdistdir}/doc/latex/pst2pdf/test.tex
%doc %{_texmfdistdir}/doc/latex/pst2pdf/test1-pdf.pdf
%doc %{_texmfdistdir}/doc/latex/pst2pdf/test1.tex
%doc %{_texmfdistdir}/doc/latex/pst2pdf/test2-pdf.pdf
%doc %{_texmfdistdir}/doc/latex/pst2pdf/test2.pdf
%doc %{_texmfdistdir}/doc/latex/pst2pdf/test2.tex
%doc %{_texmfdistdir}/doc/latex/pst2pdf/test3-pdf.pdf
%doc %{_texmfdistdir}/doc/latex/pst2pdf/test3.tex
%doc %{_texmfdistdir}/doc/latex/pst2pdf/tux.jpg

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/pst2pdf/pst2pdf.pl pst2pdf
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
