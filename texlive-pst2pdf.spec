# revision 21135
# category Package
# catalog-ctan /graphics/pstricks/scripts/pst2pdf
# catalog-date 2011-01-19 22:35:34 +0100
# catalog-license gpl
# catalog-version 0.12
Name:		texlive-pst2pdf
Version:	0.12
Release:	1
Summary:	A script to compile pstricks documents via pdftex
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/scripts/pst2pdf
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst2pdf.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst2pdf.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst2pdf.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Provides:	texlive-pst2pdf.bin = %{EVRD}
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

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

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/pst2pdf
%{_texmfdistdir}/scripts/pst2pdf/pst2pdf
%doc %{_texmfdistdir}/doc/latex/pst2pdf/Changes
%doc %{_texmfdistdir}/doc/latex/pst2pdf/Makefile
%doc %{_texmfdistdir}/doc/latex/pst2pdf/README
%doc %{_texmfdistdir}/doc/latex/pst2pdf/pst2pdf-doc.bib
%doc %{_texmfdistdir}/doc/latex/pst2pdf/pst2pdf-doc.pdf
%doc %{_texmfdistdir}/doc/latex/pst2pdf/pst2pdf-doc.tex
%doc %{_texmfdistdir}/doc/latex/pst2pdf/test1-pdf.pdf
%doc %{_texmfdistdir}/doc/latex/pst2pdf/test1.tex
%doc %{_texmfdistdir}/doc/latex/pst2pdf/test2-pdf.pdf
%doc %{_texmfdistdir}/doc/latex/pst2pdf/test2.pdf
%doc %{_texmfdistdir}/doc/latex/pst2pdf/test2.tex
%doc %{_texmfdistdir}/doc/latex/pst2pdf/test3-pdf.pdf
%doc %{_texmfdistdir}/doc/latex/pst2pdf/test3.tex
%doc %{_texmfdistdir}/doc/latex/pst2pdf/tux.jpg
#- source
%doc %{_texmfdistdir}/source/latex/pst2pdf/Makefile
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/pst2pdf/pst2pdf pst2pdf
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
