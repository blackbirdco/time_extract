# Spec - Résolution contextuelle de la metadata DURATION

## unmodifiedDurationTerm

### continousDurationTerm

```
Source : je dois trouver un stage de 6 mois
(metadata
  (durationTerm
    (unmodifiedDurationTerm
      (continousDurationTerm (numeralItem 6) (monthUnitItem mois)))))
```
unités de temps possible : minuteUnitItem, hourUnitItem, dayUnitItem, weekendUnitItem, weekUnitItem, monthUnitItem, yearUnitItem, seasonUnitItem

```
{"text" : "6 mois", "metadata" : "duration", "value" : "6", "unit" : "month"}
```

```
Source : je dois trouver un stage de 8 semaines
(metadata
  (durationTerm
    (unmodifiedDurationTerm
      (continousDurationTerm (numeralItem 8) (weekUnitItem semaine)))))
```
Calculer en mois quand c'est possible :
```
{"text" : "8 semaines", "metadata" : "duration", "value" : "2", "unit" : "month"}
```

### intervalDurationTerm

#### minimumLimitedIntervalDurationTerm

```
Source : je dois trouver un stage de plus de 6 mois
(metadata
  (durationTerm
    (unmodifiedDurationTerm
      (intervalDurationTerm
        (minimumLimitedIntervalDurationTerm
          (minimumItem plus)
          (numeralItem 6)
          (monthUnitItem mois))))))
```
```
{"text" : "plus 6 mois", "metadata" : "duration", "min_value" : "6", "unit" : "month"}
```

#### maximumLimitedIntervalDurationTerm

```
Source : je dois trouver un stage de moins de 6 mois
(metadata
  (durationTerm
    (unmodifiedDurationTerm
      (intervalDurationTerm
        (maximumLimitedIntervalDurationTerm
          (maximumItem moins)
          (numeralItem 6)
          (monthUnitItem mois))))))
```
```
{"text" : "moins 6 mois", "metadata" : "duration", "max_value" : "6", "unit" : "month"}
```

#### limitedIntervalDurationTerm

```
Source : je dois trouver un stage de 6 - 7 mois
(metadata
  (durationTerm
    (unmodifiedDurationTerm
      (intervalDurationTerm
        (limitedIntervalDurationTerm
          (minimumLimitedIntervalDurationTerm (numeralItem 6))
          (maximumLimitedIntervalDurationTerm (numeralItem 7))
          (monthUnitItem mois))))))
```

```
{"text" : "6 - 7 mois", "metadata" : "duration", "min_value" : "6", "max_value" : "7", "unit" : "month"}
```

## modifiedDurationTerm

#### approximativeDurationTerm

```
Source : je dois trouver un stage d'environ 6 mois
(metadata
  (durationTerm
    (modifiedDurationTerm
      (approximativeDurationTerm
        (approximativeItem environ)
        (unmodifiedDurationTerm
          (continousDurationTerm
            (numeralItem 6)
            (monthUnitItem mois)))))))
```

```
{"text" : "environ 6 mois", "metadata" : "duration", "approx_value" : "6", "unit" : "month"}
```