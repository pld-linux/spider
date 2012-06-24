Summary:	X11 implementation of Spider card game
Summary(de):	X11-Implementierung des Kartenspiels \"Spider\"
Summary(fr):	Implantation X11 du jeu de cartes Spider
Summary(pl):	Implementacja pasjansa Spider pod X11
Summary(tr):	Spider ka��t oyununun X11 ger�ekle�tirmesi
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
hervorragende M�glichkeiten, durch sorgf�ltige Analyse und komplexe
Manipulationen auch ung�nstige Situationen zu meistern.

%description -l fr
spider est un jeu de solitaire qui, � la diff�rence de la plupart des
autres solitaires, offre la possibilit� au joueur exp�riment� de
surmonter une mauvaise donne par une analyse pouss�e et des
manipulations complexes.

%description -l pl
Spider jest szczeg�lnie wyzywaj�cym pasjansem. W odr�nieniu od wielu
innych, daje wprawnemu graczowi mo�liwo�� przezwyci�enia nieudanego
rozdania poprzez analiz� i z�o�one manipulacje.

%description -l tr
spider iki desteli fal oyunudur. Di�er fal oyunlar�n�n aksine,
dikkatli ��z�mleme ve karma��k kullan�mlarla iyi bir oyuncunun
ka��tlar�n da��t�m�ndaki k�t� �ans� yenmesini sa�layacak olanaklar
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
