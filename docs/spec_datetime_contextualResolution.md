# Spec des sorties de la grammaire pour la normalisation JSON (datetime)

Ce document décrit les principaux arbres sémantiques générés par le module NLU. Ces arbres sémantiques correspondent à une analyse conceptuelle des expressions de type DATETIME reconnues dans les messages des users.

Un DATETIME correspond à une unité de jour dans le calendrier (e.g. *lundi, 2 janvier, demain, deuxième lundi de janvier*...). De ce fait des expressions comme *janvier*, *2016* seront traitées comme des périodes.

Ici, chaque arbre sémantique est accompagné d'une résolution contextuelle en format json. La date et/ou l'heure devront être traduits en timestamp dans la brique de résolution. Quand aucune difficulté se pose, une traduction du timestamp est donnée entre (). Le marqueur !!! indique qu'il existe une complexité de résolution nécessitant une prise de décision.

### DATETIME

#### unmodifiedDateTerm

```
Source : j'ai besoin d'un job le 2
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (dateTerm
          (unmodifiedDateTerm (calendarDateTerm (dayValueItem 2))))))))
```

```
{"text" : "2", "metadata" : "datetime", "date" : "(prochain jour ayant pour valeur 2)"}
```



```
Source : j'ai besoin d'un job le 2 janvier
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (dateTerm
          (unmodifiedDateTerm
            (calendarDateTerm
              (dayValueItem 2)
              (monthValueItem janvier))))))))
```

```
{"text" : "2 janvier", "metadata" : "datetime", "date" : "2 janvier de l'année en cours"}
```



```
Source : j'ai besoin d'un job le 2 janvier 2016
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (dateTerm
          (unmodifiedDateTerm
            (calendarDateTerm
              (dayValueItem 2)
              (monthValueItem janvier)
              (yearValueItem 2016))))))))
```

```
{"text" : "2 janvier 2016", "metadata" : "datetime", "date" : "2 janvier 2016"}
```



```
Source : j'ai besoin d'un job pour lundi
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (dateTerm
          (unmodifiedDateTerm
            (dayOfWeekTerm (firstDayOfWeekItem lundi))))))))
```

```
{"text" : "lundi", "metadata" : "datetime", "date" : "prochain jour de rang 1"}
```

* secondDayOfWeekItem : mardi 
* thirthDayOfWeekItem : mercredi
* fourthDayOfWeekItem : jeudi
* fifthDayOfWeekItem : vendredi
* sixthDayOfWeekItem : samedi
* seventhDayOfWeekItem : dimanche


```
Source : j'ai besoin d'un job lundi prochain
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (dateTerm
          (unmodifiedDateTerm
            (calendarDateTerm
              (dayOfWeekTerm (firstDayOfWeekItem lundi))
              (nextItem prochain))))))))
```

```
{"text" : "lundi prochain", "metadata" : "datetime", "date" : "prochain jour de rang 1"}
```



```
Source : j'ai besoin d'un job lundi 2
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (dateTerm
          (unmodifiedDateTerm
            (calendarDateTerm
              (dayOfWeekTerm (firstDayOfWeekItem lundi))
              (dayValueItem 2))))))))
```

```
{"text" : "lundi 2", "metadata" : "datetime", "date" : "prochain jour de rang 1 et de valeur 2"}
```



```
Source : j'ai besoin d'un job lundi 2 janvier
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (dateTerm
          (unmodifiedDateTerm
            (calendarDateTerm
              (dayOfWeekTerm (firstDayOfWeekItem lundi))
              (dayValueItem 2)
              (monthValueItem janvier))))))))
```

```
{"text" : "lundi 2 janvier", "metadata" : "datetime", "date" : "prochain jour de rang 1, de valeur 2, du mois de janvier de l'année en cours"}
```



```
Source : j'ai besoin d'un job lundi 2 janvier 2016
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (dateTerm
          (unmodifiedDateTerm
            (calendarDateTerm
              (dayOfWeekTerm (firstDayOfWeekItem lundi))
              (dayValueItem 2)
              (monthValueItem janvier)
              (yearValueItem 2016))))))))
```

```
{"text" : "lundi 2 janvier 2016", "metadata" : "datetime", "date" : "prochain jour de rang 1 un 2 janvier 2016"}
```



```
Source : j'ai besoin d'un job le deuxième lundi de janvier
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (dateTerm
          (unmodifiedDateTerm
            (calendarDateTerm
              (ordinalItem deuxieme)
              (dayOfWeekTerm (firstDayOfWeekItem lundi))
              (monthValueItem janvier))))))))
```

```
{"text" : "deuxième lundi janvier", "metadata" : "datetime", "date" : "deuxième jour de rang 1 du mois de janvier"}
```



```
Source : j'ai besoin d'un job le deuxième lundi de janvier 2016
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (dateTerm
          (unmodifiedDateTerm
            (calendarDateTerm
              (ordinalItem deuxieme)
              (dayOfWeekTerm (firstDayOfWeekItem lundi))
              (monthValueItem janvier)
              (yearValueItem 2016))))))))
```

```
{"text" : "deuxième lundi janvier 2016", "metadata" : "datetime", "date" : "deuxième jour de rang 2 du mois de janvier de l'année 2016"}
```


```
Source : j'ai besoin d'un job demain
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (dateTerm
          (unmodifiedDateTerm (dayAdverbTerm (tomorrowItem demain))))))))
```

```
{"text" : "demain", "metadata" : "datetime", "date" : "jour courant + 1 jour"}
```


```
Source : j'ai besoin d'un job aujourd'hui
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (dateTerm
          (unmodifiedDateTerm
            (dayAdverbTerm (todayItem aujourd'hui))))))))
```

```
{"text" : "aujourd'hui", "metadata" : "datetime", "date" : "jour courant"}
```


```
Source : j'avais besoin d'un job hier
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (dateTerm
          (unmodifiedDateTerm (dayAdverbTerm (yesterdayItem hier))))))))
```

```
{"text" : "hier", "metadata" : "datetime", "date" : "jour courant - 1 jour"}
```


```
Source : j'ai besoin d'un job pour après-demain
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (dateTerm
          (unmodifiedDateTerm
            (dayAdverbTerm (dayAfterTomorrowItem apres-demain))))))))
```

```
{"text" : "après-demain", "metadata" : "datetime", "date" : "jour courant + 2 jours"}
```



```
Source : j'ai besoin d'un job pour Noël
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (dateTerm
          (unmodifiedDateTerm
            (feastTerm (absoluteFeastTerm (christmasDayItem Noel)))))))))
```

```
{"text" : "Noël", "metadata" : "datetime", "date" : "25 décembre de l'année en cours"}
```

* christmasDayItem (Noël) : 25 décembre
* womenDayItem (journée de la femme) : 8 mars
* workDayItem (fête du travail) : 1er mai
* nationalDayItem (fête nationale : 14 juillet
* valentineDayItem (Saint-Valentin) : 14 février
* stpatrickDayItem (Saint-Patrick) : 17 mars
* musicDayItem (fête de la musique) : 21 juin
* halloweenDayItem  (Halloween) : 31 octobre
* newYearEveDayItem (Nouvel An) : 31 décembre
* newYearDayItem (jour de l'An) : 1er janvier
* toussaintDayItem (Toussaint) : 1er novembre
* armisticeDayItem (armistice) : 8 mai
* assomptionDayItem (Assomption) : 15 août


```
Source : j'ai besoin d'un job pour Pâques
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (dateTerm
          (unmodifiedDateTerm
            (feastTerm (relativeFeastTerm (easterDayItem Paques)))))))))
```

* easterDayItem                   -> "Pâques"
* grandmotherDayItem              -> "fête des grands-mères"
* motherDayItem                   -> "fête des mères"
* fatherDayItem                   -> "fête des pères"
* carnivalDayItem                 -> "Carnaval" | "mardi gras"
* easterMondayDayItem             -> "lundi de Pâques"
* ascensionDayItem                -> "Ascension"
* palmSundayDayItem               -> "Rameaux" | "fête des Rameaux"
* pentecostDayItem                -> "Pentecôte"
* goodFridayItem                  -> "vendredi saint"

```
Source : j'ai besoin d'un job pour la rentrée
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (dateTerm
          (unmodifiedDateTerm (eventTerm (schoolStartItem rentree))))))))
```

```
{"text" : "2", "metadata" : "datetime", "date" : "(référentiel avec mise à jour de la date de rentrée)"}
```

#### modifiedDateTerm

```
Source : j'ai besoin d'un job avant lundi
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (dateTerm
          (modifiedDateTerm
            (beforeDateTerm
              (beforeItem avant)
              (unmodifiedDateTerm
                (dayOfWeekTerm (firstDayOfWeekItem lundi))))))))))
```

```
{"text" : "2", "metadata" : "datetime", "date" : "(!!!)"}
```



```
Source : j'ai besoin d'un job après lundi
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (dateTerm
          (modifiedDateTerm
            (afterDateTerm
              (afterItem apres)
              (unmodifiedDateTerm
                (dayOfWeekTerm (firstDayOfWeekItem lundi))))))))))
```

```
{"text" : "2", "metadata" : "datetime", "date" : "(!!!)"}
```

```
Source : j'ai besoin d'un job vers lundi
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (dateTerm
          (modifiedDateTerm
            (approximativeDateTerm
              (approximativeItem vers)
              (unmodifiedDateTerm
                (dayOfWeekTerm (firstDayOfWeekItem lundi))))))))))
```

```
{"text" : "2", "metadata" : "datetime", "date" : "(!!!)"}
```


```
Source : j'ai besoin d'un job sauf lundi
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (dateTerm
          (modifiedDateTerm
            (negativeDateTerm
              (negativeItem sauf)
              (unmodifiedDateTerm
                (dayOfWeekTerm (firstDayOfWeekItem lundi))))))))))
```

```
{"text" : "2", "metadata" : "datetime", "date" : "(!!!)"}
```

```
Source : j'ai besoin d'un job uniquement lundi
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (dateTerm
          (modifiedDateTerm
            (constraintDateTerm
              (constraintItem uniquement)
              (unmodifiedDateTerm
                (dayOfWeekTerm (firstDayOfWeekItem lundi))))))))))
```

```
{"text" : "2", "metadata" : "datetime", "date" : "(!!!)"}
```

#### vectorDateTerm

```
Source : j'ai besoin d'un job dans 2 jours
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (dateTerm
          (vectorDateTerm
            (futureVectorDateTerm
              (futureVectorPreposition dans)
              (distanceVectorDateTerm
                (numeralItem 2)
                (dayUnitItem jour)))))))))
```

```
{"text" : "dans 2 jour", "metadata" : "datetime", "date" : "(jour courant + 2 jours)"}
```

```
Source : j'ai besoin d'un job dans 2 semaines
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (dateTerm
          (vectorDateTerm
            (futureVectorDateTerm
              (futureVectorPreposition dans)
              (distanceVectorDateTerm
                (numeralItem 2)
                (weekUnitItem semaine)))))))))
```

```
{"text" : "dans 2 semaine", "metadata" : "datetime", "date" : "(jour courant + 15 jours)"}
```

```
Source : j'ai besoin d'un job dans 2 mois
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (dateTerm
          (vectorDateTerm
            (futureVectorDateTerm
              (futureVectorPreposition dans)
              (distanceVectorDateTerm
                (numeralItem 2)
                (monthUnitItem mois)))))))))
```

```
{"text" : "dans 2 mois", "metadata" : "datetime", "date" : "(jour courant + 30 jours)"}
```

```
Source : j'ai besoin d'un job dans 2 ans
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (dateTerm
          (vectorDateTerm
            (futureVectorDateTerm
              (futureVectorPreposition dans)
              (distanceVectorDateTerm
                (numeralItem 2)
                (yearUnitItem an)))))))))
```

```
{"text" : "dans 2 an", "metadata" : "datetime", "date" : "(jour courant + 730)"}
```

il y a 2 jours (marche pas à cause du pb des MWE)
il y a 2 semaines (marche pas à cause du pb des MWE)
il y a 2 mois (marche pas à cause du pb des MWE)
il y a 2 ans (marche pas à cause du pb des MWE)

#### urgencyDateTerm

```
Souce : j'ai besoin d'un job maintenant
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (dateTerm (urgencyDateTerm (urgencyItem maintenant)))))))
```

```
{"text" : "maintenant", "metadata" : "datetime", "date" : "(!!!)"}
```

#### indeterminateDateTerm

```
Source : j'ai besoin d'un job mais je ne sais pas quand
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (dateTerm
          (indeterminateDateTerm
            (knownVerbItem savoir)
            (negationItem pas)
            (whenItem quand)))))))
```

```
{"text" : "savoir pas quand", "metadata" : "datetime", "date" : "null"}
```

#### unmodifiedHourTerm

```
Source : il y a quoi au ciné à 14 heure ?
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (hourTerm
          (unmodifiedHourTerm
            (numericHourTerm (hourValueItem 14) (hourUnitItem heure))))))))
```

```
{"text" : "14 heure", "metadata" : "datetime", "hour" : "(14:00:00)"}
```

```
Source : il y a quoi au ciné à 14 heure 30 ?
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (hourTerm
          (unmodifiedHourTerm
            (numericHourTerm
              (hourValueItem 14)
              (hourUnitItem heure)
              (minuteValueItem 30))))))))
```

```
{"text" : "14 heure 30", "metadata" : "datetime", "hour" : "(14:30:00)"}
```

2 heure et demi (marche pas à cause du pb des MWEs)
2 heure et quart (marche pas à cause du pb des MWEs)
2 heure moins le quart (marche pas à cause du pb des MWEs)

```
Source : il y a quoi au ciné à deux heures ?
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (hourTerm
          (unmodifiedHourTerm
            (numericHourTerm
              (hourLetterItem deux)
              (hourUnitItem heure))))))))
```

```
{"text" : "deux heure", "metadata" : "datetime", "date" : "(14:00:00)"}
```

```
Source : il y a quoi au ciné au petit-déjeuner ?
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (hourTerm
          (unmodifiedHourTerm
            (lunchTerm (breakfastTimeItem petit-dejeuner))))))))
```

```
{"text" : "petit-déjeuner", "metadata" : "datetime", "hour" : "(!!!)"}
```

```
Source : il y a quoi au ciné au déjeuner ?
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (hourTerm
          (unmodifiedHourTerm (lunchTerm (lunchTimeItem dejeuner))))))))
```

```
{"text" : "déjeuner", "metadata" : "datetime", "hour" : "(!!!)"}
```

```
Source : il y a quoi au ciné au goûter ?
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (hourTerm
          (unmodifiedHourTerm (lunchTerm (teaTimeItem gouter))))))))
```

```
{"text" : "goûter", "metadata" : "datetime", "hour" : "(!!!)"}
```

happy hour (marche pas à cause du pb des MWEs)

```
Source : il y a quoi au ciné au dîner ? 
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (hourTerm
          (unmodifiedHourTerm (lunchTerm (dinnerTimeItem diner))))))))
```

```
{"text" : "dîner", "metadata" : "datetime", "hour" : "(!!!)"}
```

```
Source : il y a quoi au ciné à midi ?
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (hourTerm
          (unmodifiedHourTerm (hourNameTerm (middayItem midi))))))))
```

```
{"text" : "midi", "metadata" : "datetime", "hour" : "(12:00:00)"}
```

```
Source : il y a quoi au ciné à minuit ?
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (hourTerm
          (unmodifiedHourTerm (hourNameTerm (midnightItem minuit))))))))
```

```
{"text" : "minuit", "metadata" : "datetime", "hour" : "(24:00:00)"}
```

midi et demi (marche pas à cause du pb des MWEs)
midi et quart (marche pas à cause du pb des MWEs)
midi moins le quart (marche pas à cause du pb des MWEs)

```
Source : matin
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (hourTerm
          (unmodifiedHourTerm
            (dayPartTerm
              (morningTerm (fullMorningTerm (morningItem matin))))))))))
```

```
{"text" : "matin", "metadata" : "datetime", "hour" : "(!!!)"}
```

```
Source : ce matin
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (hourTerm
          (modifiedHourTerm
            (currentHourTerm
              (currentItem ce)
              (unmodifiedHourTerm
                (dayPartTerm
                  (morningTerm (fullMorningTerm (morningItem matin))))))))))))
```

```
{"text" : "ce matin", "metadata" : "datetime", "date" : "(jour courant)", "hour" : "(!!!)"}
```

```
Source : après-midi
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (hourTerm
          (unmodifiedHourTerm
            (dayPartTerm
              (aftertnoonTerm
                (fullAfternoonTerm (aftertnoonItem apres-midi))))))))))
```

```
{"text" : "après-midi", "metadata" : "datetime", "hour" : "(!!!)"}
```

```
Source : soir
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (hourTerm
          (unmodifiedHourTerm
            (dayPartTerm
              (eveningTerm (fullEveningTerm (eveningItem soir))))))))))
```

```
{"text" : "soir", "metadata" : "datetime", "hour" : "(!!!)"}
```

```
Source : nuit
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (hourTerm
          (unmodifiedHourTerm
            (dayPartTerm
              (nightTerm (fullNightTerm (nightItem nuit))))))))))
```

```
{"text" : "nuit", "metadata" : "datetime", "hour" : "(!!!)"}
```

```
Source : début de matinée
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (hourTerm
          (unmodifiedHourTerm
            (dayPartTerm
              (morningTerm
                (startMorningTerm
                  (startItem debut)
                  (morningItem matinee))))))))))
```

```
{"text" : "début matinée", "metadata" : "datetime", "hour" : "(!!!)"}
```

```
Source : milieu de matinée
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (hourTerm
          (unmodifiedHourTerm
            (dayPartTerm
              (morningTerm
                (midMorningTerm
                  (midItem milieu)
                  (morningItem matinee))))))))))
```

```
{"text" : "milieu matinée", "metadata" : "datetime", "hour" : "(!!!)"}
```

```
Source : fin de matinée
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (hourTerm
          (unmodifiedHourTerm
            (dayPartTerm
              (morningTerm
                (endMorningTerm (endItem fin) (morningItem matinee))))))))))
```

```
{"text" : "fin matinée", "metadata" : "datetime", "hour" : "(!!!)"}
```

```
Source : première partie de soirée
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (hourTerm
          (unmodifiedHourTerm
            (dayPartTerm
              (eveningTerm
                (startEveningTerm
                  (startOrdinalEveningItem premier)
                  (partItem partie)
                  (eveningItem soiree))))))))))
```

```
{"text" : "première partie soirée", "metadata" : "datetime", "hour" : "(!!!)"}
```

```
Source : deuxième partie de soirée
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (hourTerm
          (unmodifiedHourTerm
            (dayPartTerm
              (eveningTerm
                (endEveningTerm
                  (endOrdinalEveningItem deuxieme)
                  (partItem partie)
                  (eveningItem soiree))))))))))
```

```
{"text" : "deuxième partie soirée", "metadata" : "datetime", "hour" : "(!!!)"}
```

#### modifiedHourTerm

```
Source : avant midi
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (hourTerm
          (modifiedHourTerm
            (beforeHourTerm
              (beforeItem avant)
              (unmodifiedHourTerm (hourNameTerm (middayItem midi))))))))))
```

```
{"text" : "avant midi", "metadata" : "datetime", "hour" : "(!!!)"}
```

```
Source : après midi
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (hourTerm
          (modifiedHourTerm
            (afterHourTerm
              (afterItem apres)
              (unmodifiedHourTerm (hourNameTerm (middayItem midi))))))))))
```

```
{"text" : "après midi", "metadata" : "datetime", "hour" : "(!!!)"}
```

```
Source : vers midi
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (hourTerm
          (modifiedHourTerm
            (approximativeHourTerm
              (approximativeItem vers)
              (unmodifiedHourTerm (hourNameTerm (middayItem midi))))))))))
```

```
{"text" : "vers midi", "metadata" : "datetime", "hour" : "(!!!)"}
```

```
Source : uniquement à midi
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (hourTerm
          (modifiedHourTerm
            (constraintHourTerm
              (constraintItem uniquement)
              (unmodifiedHourTerm (hourNameTerm (middayItem midi))))))))))
```

```
{"text" : "uniquement midi", "metadata" : "datetime", "hour" : "(!!!)"}
```

```
Source : sauf à midi
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (hourTerm
          (modifiedHourTerm
            (negativeHourTerm
              (negativeItem sauf)
              (unmodifiedHourTerm (hourNameTerm (middayItem midi))))))))))
```

```
{"text" : "sauf midi", "metadata" : "datetime", "hour" : "(!!!)"}
```

#### vectorHourTerm

```
Source : dans 2 heures
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (hourTerm
          (vectorHourTerm
            (futureVectorHourTerm
              (futureVectorPreposition dans)
              (distanceVectorHourTerm
                (numeralItem 2)
                (hourUnitItem heure)))))))))
```

```
{"text" : "dans 2 heure", "metadata" : "datetime", "hour" : "(heure actuelle + 2 h)"}
```

#### Combinaison de dateTerm + hourTerm

```
Source : lundi à 14 heure
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (dateTerm
          (unmodifiedDateTerm
            (dayOfWeekTerm (firstDayOfWeekItem lundi))))
        (hourTerm
          (unmodifiedHourTerm
            (numericHourTerm (hourValueItem 14) (hourUnitItem heure))))))))
```

```
{"text" : "lundi 14 heure", "metadata" : "datetime", "date" : "(prochain jour ayant pour rang 1)", "hour" : "14:00:00"}
```

```
Source : à 14 heure lundi
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeElementTerm
        (hourTerm
          (unmodifiedHourTerm
            (numericHourTerm (hourValueItem 14) (hourUnitItem heure))))
        (dateTerm
          (unmodifiedDateTerm
            (dayOfWeekTerm (firstDayOfWeekItem lundi))))))))
```

```
{"text" : "14 heure lundi", "metadata" : "datetime", "date" : "(prochain jour ayant pour rang 1)", "hour" : "14:00:00"}
```

#### datetimeAlternativeElementTerm

```
Source : lundi ou mardi
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeAlternativeElementTerm
        (datetimeElementTerm
          (dateTerm
            (unmodifiedDateTerm
              (dayOfWeekTerm (firstDayOfWeekItem lundi)))))
        (alternativeItem ou)
        (datetimeElementTerm
          (dateTerm
            (unmodifiedDateTerm
              (dayOfWeekTerm (secondDayOfWeekItem mardi)))))))))
```

```
{"text" : "lundi ou mardi", "metadata" : "datetime", "date" : "(!!!)"}
```

#### datetimeGroupElementTerm

```
Source : lundi et mardi
(metadata
  (datetimeTerm
    (datetimeGeneralTerm
      (datetimeGroupElementTerm
        (datetimeElementTerm
          (dateTerm
            (unmodifiedDateTerm
              (dayOfWeekTerm (firstDayOfWeekItem lundi)))))
        (groupItem et)
        (datetimeElementTerm
          (dateTerm
            (unmodifiedDateTerm
              (dayOfWeekTerm (secondDayOfWeekItem mardi)))))))))
```

```
{"text" : "lundi et mardi", "metadata" : "datetime", "date" : "(!!!)"}
```

#### datetimeTravelTerm

```
Source : partir lundi
(metadata
  (datetimeTerm
    (datetimeTravelTerm
      (departureDateTerm
        (departureItem partir)
        (datetimeGeneralTerm
          (datetimeElementTerm
            (dateTerm
              (unmodifiedDateTerm
                (dayOfWeekTerm (firstDayOfWeekItem lundi))))))))))
```

```
{"text" : "partir lundi", "metadata" : "datetime", "departure_date" : "(prochain jour ayant pour rang 1)"}
```


```
Source : revenir lundi
(metadata
  (datetimeTerm
    (datetimeTravelTerm
      (returnDateTerm
        (returnItem revenir)
        (datetimeGeneralTerm
          (datetimeElementTerm
            (dateTerm
              (unmodifiedDateTerm
                (dayOfWeekTerm (firstDayOfWeekItem lundi))))))))))
```

```
{"text" : "revenir lundi", "metadata" : "datetime", "return_date" : "(prochain jour ayant pour rang 1)"}
```

```
Source : partir lundi et revenir mardi
(metadata
  (datetimeTerm
    (datetimeTravelTerm
      (departureDateTerm
        (departureItem partir)
        (datetimeGeneralTerm
          (datetimeElementTerm
            (dateTerm
              (unmodifiedDateTerm
                (dayOfWeekTerm (secondDayOfWeekItem mardi)))))))
      (groupItem et)
      (returnDateTerm
        (returnItem revenir)
        (datetimeGeneralTerm
          (datetimeElementTerm
            (dateTerm
              (unmodifiedDateTerm
                (dayOfWeekTerm (firstDayOfWeekItem lundi))))))))))
```

```
{"text" : "partir lundi et revenir mardi", "metadata" : "datetime", "departure_date" : "(prochain jour ayant pour rang 1)", "return_date" : "(prochain jour ayant pour rang 2)"}
```