-- counts words in a document

words = 0

wordcount = {
  Str = function(el)
    -- we don't count a word if it's entirely punctuation:
    if el.text:match("%P") then
        words = words + 1
    end
  end,

  Code = function(el)
    _,n = el.text:gsub("%S+","")
    words = words + n
  end,

  CodeBlock = function(el)
    _,n = el.text:gsub("%S+","")
    words = words + n
  end
}

function Pandoc(doc)
    -- walk through the document to count words
    pandoc.walk_block(pandoc.Div(doc.blocks), wordcount)
    -- set the word count in the document's metadata
    doc.meta['wordcount'] = pandoc.MetaString(tostring(words))
    -- return the modified document
    return doc
end
