// Sample Google Apps Script: normalize and trim values in the active sheet
function normalizeSheet() {
  var sheet = SpreadsheetApp.getActiveSheet();
  var range = sheet.getDataRange();
  var values = range.getValues();
  for (var r = 0; r < values.length; r++) {
    for (var c = 0; c < values[r].length; c++) {
      if (typeof values[r][c] === 'string') {
        values[r][c] = values[r][c].trim();
      }
    }
  }
  range.setValues(values);
}
