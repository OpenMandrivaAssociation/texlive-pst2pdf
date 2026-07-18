%global tl_name pst2pdf
%global tl_revision 56172
%global tl_bin_links pst2pdf:%{_texmfdistdir}/scripts/pst2pdf/pst2pdf.pl

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.20
Release:	%{tl_revision}.1
Summary:	A script to compile PSTricks documents via pdfTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/scripts/pst2pdf
License:	gpl2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst2pdf.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst2pdf.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(pst2pdf.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
The script extracts the preamble of the document and runs all
\begin{postscript}...\end{postscript}
\begin{pspicture}...\end{pspicture} and \pspicture...\endpspicture
separately through LaTeX with the same preamble as the original
document; thus it creates EPS, PNG and PDF files of these snippets. In a
final pdfLaTeX run the script replaces the environments with
\includegraphics to include the processed snippets. Detail documentation
is acquired from the document itself via Perldoc.

