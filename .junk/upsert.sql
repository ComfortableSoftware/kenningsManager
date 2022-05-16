INSERT INTO [entries] ([comment], [grammar], [insertName], [keys], [linkifyFixedText], [lowerCaseFixedText], [project], [stringToInsert], [upperCaseSelectedText])
  VALUES ("Generic comment starter", "*", "Hash Comment", "alt-ctrl-m°c", True, True, "kenningsManager", "# * ", False)
  ON CONFLICT ([comment], [grammar], [insertName], [keys], [linkifyFixedText], [lowerCaseFixedText], [project], [stringToInsert], [upperCaseSelectedText], ) DO UPDATE SET
    [comment] = EXCLUDED.[comment],
    [grammar] = EXCLUDED.[grammar],
    [insertName] = EXCLUDED.[insertName],
    [keys] = EXCLUDED.[keys],
    [linkifyFixedText] = EXCLUDED.[linkifyFixedText],
    [lowerCaseFixedText] = EXCLUDED.[lowerCaseFixedText],
    [project] = EXCLUDED.[project],
    [stringToInsert] = EXCLUDED.[stringToInsert],
    [upperCaseSelectedText] = EXCLUDED.[upperCaseSelectedText];


IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION

STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION
