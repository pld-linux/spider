Summary:	X11 implementation of Spider card game
Summary(de):	X11-Implementierung des Kartenspiels \"Spider\"
Summary(fr):	Implantation X11 du jeu de cartes Spider
Summary(pl):	Implementacja pasjansa Spider pod X11
Summary(tr):	Spider kaðýt oyununun X11 gerçekleþtirmesi
Name:		spider
Version:	1.1
Release:	1
License:	distributable
Group:		X11/Applications/Games
Source0:	ftp://sunsite.unc.edu/pub/Linux/games/solitaires/%{name}.tar.Z
# Source0-md5:	3ffbe6417b497531ff5b46cab7db311f
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
spider is a particularly challenging double-deck solitaire. Unlike
most solitaires, it provides extraordinary opportunities for the
skillful player to overcome bad luck in the deal by means of careful
analysis and complex manipulations.

%description -l de
spider ist ein ganz besonders anspruchsvolles Solitaire mit doppelten
Karten. Anders als andere Solitaires bietet es dem geschickten Spieler
hervorragende Möglichkeiten, durch sorgfältige Analyse und komplexe
Manipulationen auch ungünstige Situationen zu meistern.

%description -l fr
spider est un jeu de solitaire qui, à la différence de la plupart des
autres solitaires, offre la possibilité au joueur expérimenté de
surmonter une mauvaise donne par une analyse poussée et des
manipulations complexes.

%description -l pl
Spider jest szczególnie wyzywaj±cym pasjansem. W odró¿nieniu od wielu
innych, daje wprawnemu graczowi mo¿liwo¶æ przezwyciê¿enia nieudanego
rozdania poprzez analizê i z³o¿one manipulacje.

%description -l tr
spider iki desteli fal oyunudur. Diðer fal oyunlarýnýn aksine,
dikkatli çözümleme ve karmaþýk kullanýmlarla iyi bir oyuncunun
kaðýtlarýn daðýtýmýndaki kötü þansý yenmesini saðlayacak olanaklar
sunar.

%prep
%setup -q -n spider

%build
xmkmf -DOverrideDefs=No

%{__make} \
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
