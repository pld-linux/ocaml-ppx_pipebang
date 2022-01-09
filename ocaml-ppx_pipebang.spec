#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	A ppx rewriter that inlines reverse application operators |> and |!
Summary(pl.UTF-8):	Moduł przepisujący ppx rozwijający w miejscu operatory odwrotnej aplikacji |> i |!
Name:		ocaml-ppx_pipebang
Version:	0.14.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/ppx_pipebang/tags
Source0:	https://github.com/janestreet/ppx_pipebang/archive/v%{version}/ppx_pipebang-%{version}.tar.gz
# Source0-md5:	50ce0e9f45bea5339bf1dbcdb53fbc5f
URL:		https://github.com/janestreet/ppx_pipebang
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-ppxlib-devel >= 0.11.0
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
A ppx rewriter that inlines reverse application operators |> and |!.

This package contains files needed to run bytecode executables using
ppx_pipebang library.

%description -l pl.UTF-8
Moduł przepisujący ppx rozwijający w miejscu operatory odwrotnej
aplikacji |> i |!.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki ppx_pipebang.

%package devel
Summary:	A ppx rewriter that inlines reverse application operators |> and |! - development part
Summary(pl.UTF-8):	Moduł przepisujący ppx rozwijający w miejscu operatory odwrotnej aplikacji |> i |! - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-ppxlib-devel >= 0.11.0

%description devel
This package contains files needed to develop OCaml programs using
ppx_pipebang library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki ppx_pipebang.

%prep
%setup -q -n ppx_pipebang-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_pipebang/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/ppx_pipebang

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md README.md
%dir %{_libdir}/ocaml/ppx_pipebang
%attr(755,root,root) %{_libdir}/ocaml/ppx_pipebang/ppx.exe
%{_libdir}/ocaml/ppx_pipebang/META
%{_libdir}/ocaml/ppx_pipebang/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/ppx_pipebang/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/ppx_pipebang/*.cmi
%{_libdir}/ocaml/ppx_pipebang/*.cmt
%{_libdir}/ocaml/ppx_pipebang/*.cmti
%{_libdir}/ocaml/ppx_pipebang/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/ppx_pipebang/ppx_pipebang.a
%{_libdir}/ocaml/ppx_pipebang/*.cmx
%{_libdir}/ocaml/ppx_pipebang/*.cmxa
%endif
%{_libdir}/ocaml/ppx_pipebang/dune-package
%{_libdir}/ocaml/ppx_pipebang/opam
