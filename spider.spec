Summary:	X11 implementation of Spider card game
Summary(de.UTF-8):	X11-Implementierung des Kartenspiels \"Spider\"
Summary(fr.UTF-8):	Implantation X11 du jeu de cartes Spider
Summary(pl.UTF-8):	Implementacja pasjansa Spider pod X11
Summary(tr.UTF-8):	Spider kağıt oyununun X11 gerçekleştirmesi
Name:		spider
Version:	1.1
Release:	2
License:	distributable
Group:		X11/Applications/Games
Source0:	ftp://sunsite.unc.edu/pub/Linux/games/solitaires/%{name}.tar.Z
# Source0-md5:	3ffbe6417b497531ff5b46cab7db311f
Patch0:		%{name}-c.patch
BuildRequires:	xorg-cf-files
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-util-imake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
spider is a particularly challenging double-deck solitaire. Unlike
most solitaires, it provides extraordinary opportunities for the
skillful player to overcome bad luck in the deal by means of careful
analysis and complex manipulations.

%description -l de.UTF-8
spider ist ein ganz besonders anspruchsvolles Solitaire mit doppelten
Karten. Anders als andere Solitaires bietet es dem geschickten Spieler
hervorragende Möglichkeiten, durch sorgfältige Analyse und komplexe
Manipulationen auch ungünstige Situationen zu meistern.

%description -l fr.UTF-8
spider est un jeu de solitaire qui, à la différence de la plupart des
autres solitaires, offre la possibilité au joueur expérimenté de
surmonter une mauvaise donne par une analyse poussée et des
manipulations complexes.

%description -l pl.UTF-8
Spider jest szczególnie wyzywającym pasjansem. W odróżnieniu od wielu
innych, daje wprawnemu graczowi możliwość przezwyciężenia nieudanego
rozdania poprzez analizę i złożone manipulacje.

%description -l tr.UTF-8
spider iki desteli fal oyunudur. Diğer fal oyunlarının aksine,
dikkatli çözümleme ve karmaşık kullanımlarla iyi bir oyuncunun
kağıtların dağıtımındaki kötü şansı yenmesini sağlayacak olanaklar
sunar.

%prep
%setup -q -n spider
%patch0 -p1

%build
xmkmf -DOverrideDefs=No

%{__make} \
	CC="%{__cc}" \
	CDEBUGFLAGS="%{rpmcflags}" \
	HELPDIR="%{_datadir}/spider"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir}/man1

install -d $RPM_BUILD_ROOT%{_datadir}/spider
install doc.* $RPM_BUILD_ROOT%{_datadir}/spider

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/spider
%{_datadir}/spider
%{_mandir}/man1/spider.1x*
