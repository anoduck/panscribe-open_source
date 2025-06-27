--[[

wordcount.lua
=============================================================================

A Pandoc Lua filter that counts the words in a document body. This is useful
for prose manuscripts (short stories, novels) where an approximate word
count is required by Standard Manuscript Format.

The filter:
- Counts words in the main text.
- Excludes strings that are only punctuation (e.g., '---' for scene breaks).
- Formats numbers over 999 with a comma (e.g., 1,000).
- Sets the 'wordcount' metadata variable for use in a template.

See also: Line Count filter for poetry.

Usage
--------------------------------------------------------------------------------

pandoc --defaults=story.yml "my-story.md" -o "my-story.pdf"

Note: This filter is typically used with a defaults file (e.g., story.yml)
that calls it automatically. The template (e.g., story.latex) should use
the '$wordcount$' variable to display the count.

]]--

words = 0

-- Function to format a number with thousands separators (commas)
function format_with_commas(n)
  local s = tostring(n)
  local len = #s
  if len < 4 then return s end
  local i = len % 3
  if i == 0 then i = 3 end
  local result = s:sub(1, i)
  for j = i + 1, len, 3 do
    result = result .. ',' .. s:sub(j, j + 2)
  end
  return result
end

wordcount = {
  Str = function(el)
    -- Count a string as a word only if it contains at least one
    -- non-punctuation character. This correctly excludes scene separators
    -- ('---') and other punctuation-only strings.
    if el.text:match("%P") then
        words = words + 1
    end
  end
}

function Pandoc(doc)
    -- walk through the document to count words
    pandoc.walk_block(pandoc.Div(doc.blocks), wordcount)
    -- format the word count with commas
    local formatted_words = format_with_commas(words)
    -- set the word count in the document's metadata
    doc.meta['wordcount'] = pandoc.MetaString(formatted_words)
    -- return the modified document
    return doc
end
