

import kenningsManager.VARS as V



# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * Start of __main__
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def __main__():
  # fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
  V.zeroThis()
  _SQLStr_ = f"""
SELECT DISTINCT [keys] FROM [entries]
  ORDER BY [keys];
"""
  _result_ = dict(V.SQL.doSQLOne(
      cursor_=V.DB_CURSOR,
      SQLStr_=_SQLStr_,
  ))
  with (open(V.INIT_OUTPUT_NAME, "tw") as V.FD_OUT):
    while (
        (_result_ is not None)
    ):
      V.INIT_ENTRY_STR(
          keysIn_=_result_["keys"]
      )
      _result_ = V.SQL.getNextResult(
          cursor_=V.DB_CURSOR,
      )
    V.FD_OUT.write(V.THIS_OUTPUT_STR)
  # fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * End of __main__
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
