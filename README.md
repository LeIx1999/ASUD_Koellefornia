# ASUD_Koellefornia #
## Spam Klassifizierung ##
### Email ###

Als Spam bezeichnet man jegliche unerwünschte Nachricht, die häufig in Form von Werbung im eigenen Postfach landet. Besonders häufig tritt das Problem im Kontext von E-Mails auf. Neben ungefährlichen Werbenachrichten, fallen auch Phishing Nachrichten unter den Überbegriff des Spams. Diese besondere Kategorie massenhaft verschickter Nachrichten ist ein beliebtes Mittel, um Internet-Nutzer in die Falle zu locken, ihren Computer mit Viren oder Trojanern zu kapern und in der Folge Daten zu stehlen, die Identität des Nutzers zu übernehmen oder Ressourcen des Computers zu beanspruchen. Ein guter Spam-Filter kann hierbei helfen, jegliche Arten von Spam bereits beim Eingang der Nachricht zu erkennen und in einen spezifischen Ordner zu verschieben, wodurch das Risiko sinkt, Opfer einer Datenfalle zu werden. 

 

### Social Media ### 

Als Spam bezeichnet man jegliche unerwünschte Nachricht, die häufig in Form von Werbung im eigenen Postfach landet. Auf Social-Media-Plattformen wie Instagram gibt es neben diesen sog. Direct-Messages zusätzlich das Problem von Spam-Nachrichten in der Kommentarfunktion unter Beiträgen. Diese stammen häufig von sog. Instagram-Bots also Computerprogrammen, die quasi autonom Accounts folgen können, Direct-Messages senden oder eben Kommentare schreiben. Häufig sind in den Profilen der Bots Links enthalten, die Nutzer auf dubiose Webseiten weiterleiten. Auf diesem Wege können auch sog. Phishing, welches man meist von E-Mails kennt, auf Social Media betrieben werden. Diese besondere Kategorie massenhaft verschickter Nachrichten ist ein beliebtes Mittel, um Internet-Nutzer in die Falle zu locken, ihren Computer mit Viren oder Trojanern zu kapern und in der Folge Daten zu stehlen, die Identität des Nutzers zu übernehmen oder Ressourcen des Computers zu beanspruchen. Ein guter Spam-Filter kann hierbei helfen, jegliche Arten von Spam bereits beim Eingang der Nachricht zu erkennen und sie zu löschen, wodurch das Risiko sinkt, Opfer einer Datenfalle zu werden. 

 

### Business Understanding ###
- Formulierung von konkreten Fragestellungen und Zielen  
- Abgleich von Aufgaben und Erwartungen 
- Vereinbarung eines Vorgehens/einer Planung  
- Identifikation von wichtigen Einflussfaktoren  
- Verständnis des Geschäftsmodells  
- Definition von Erfolgskriterien 

### Email ###

Besonders in Unternehmen können Phishing-Nachrichten großen Schaden anrichten, da nicht nur die Daten des Nutzers, welcher die Nachricht geöffnet hat, gestohlen werden können, sondern auch Unternehmensdaten und Kundendaten für den Versender der Phishing-Nachricht einsehbar sind. Unternehmen sind dafür verantwortlich, für die Sicherheit der Kundendaten Sorge zu tragen, weshalb neben dem Verlust von Unternehmensinternen und ggf. auch geheimen Daten, vor allem die juristische Verfolgung des Kundendatenverlustes sowie der damit einhergehende Vertrauensverlust in das Unternehmen eine schwere Last darstellt.  

Um diesem Problem Abhilfe zu schaffen, ist es das Ziel des Projektes, auf Basis von Textnachrichten einen Spam-Filter zu entwickeln, welcher Texte in die Kategorien „Spam“ und „kein Spam“ einteilt und so das automatische Verschieben von unerwünschten oder gefährlichen Nachrichten in einen gesonderten Ordner erlaubt. Hierfür werden mit Hilfe eines Machine Learning Modells bereits klassifizierte Textnachrichten analysiert und Merkmale von Spam-Nachrichten herausgearbeitet. Das Modell wird auf englischer Sprache trainiert und kann somit auch nur für die Klassifizierung englischsprachiger Nachrichten eingesetzt werden. 

 

### Social Media ###

Die in der Einleitung erläuterten Bots sind für Unternehmen oder Influencer Fluch und Segen zugleich. Einerseits werden sie gezielt eingesetzt, um mit einem Profil eine größere Reichweite zu erzielen, indem Follower, Likes und Kommentare quasi gekauft werden. Die höhere Zahl dieser Parameter führt dazu, dass mehr Leute auf das Profil stoßen und somit auch mehr „echte“ Nutzer als Follower gewonnen werden können. Bemüht man sich jedoch, mit seinem Profil und seinen Posts einen seriösen Eindruck zu vermitteln oder ernste Themen anzusprechen, wie dies z. B. auf dem Instagram-Profil von Nachrichtensendern der Fall ist, können die Bots regelrecht zur Plage werden, da bspw. plötzlich unter Posts jede Menge Kommentare von Bot-Profilen sind, die Sex anbieten. 

Um diesem Problem Abhilfe zu schaffen, ist es das Ziel des Projektes, auf Basis von Textnachrichten einen Spam-Filter zu entwickeln, welcher Texte in die Kategorien „Spam“ und „kein Spam“ einteilt und so das automatische unmittelbare Löschen von unerwünschten oder gefährlichen Nachrichten in erlaubt. Hierfür werden mit Hilfe eines Machine Learning Modells bereits klassifizierte Textnachrichten analysiert und Merkmale von Spam-Nachrichten herausgearbeitet. Das Modell wird auf englischer Sprache trainiert und kann somit auch nur für die Klassifizierung englischsprachiger Nachrichten eingesetzt werden. 

 

### Data Understanding ###
- Betrachtung des Datenbestands 
- Auswertung der Datenverfügbarkeit, -reliabilität, -qualität  
- (Statistische) Auffälligkeiten in den Daten  
- Abstimmung zum Datenschutz 

Der für das Projekt genutzte Datensatz stammt von der Online-Community-Plattform Kaggle. Er enthält 5.157 Beispielnachrichten, von denen 87 Prozent der Kategorie „kein Spam“ und 13 Prozent der Kategorie „Spam“ zugeordnet sind. Ergänzend werden noch 50 eigene Nachrichten zur Überprüfung der Vorhersageleistung des Machine Learning Modells genutzt. Diese bestehen zu 50 Prozent aus Spam-Nachrichten. Der Datensatz besteht aus den zwei Variablen „Category” und „Message”. „Category” ist die kategorische binäre abhängige Variable mit den Ausprägungen „kein Spam“ und „Spam“. „Message” ist eine kategorische unabhängige Variable, in der der Text der Spam Nachricht gespeichert ist. Beide Variablen sind für jeden Datensatz befüllt. Es gibt folglich keine Null-Werte. 

Bei der Betrachtung des Kaggle-Datensatzes fällt auf, dass die Nachrichten sehr umgangssprachlich formuliert sind. So wird das Wort „you“ zumeist durch „u“ oder „are“ durch „r“ abgekürzt. Hierdurch wird eine Betrachtung von Rechtschreibfehlern als Anzeichen einer Spam-Nachricht nahezu unmöglich. Ebenfalls fehlen in den Nachrichten sowohl Anreden als auch Absender.  
