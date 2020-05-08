class Lexicon
  Pair=Struct.new(:token,:word)
  @@dict={}
  
  def initialize()
    update_dict("north south east west down up left right back",:direction)
    update_dict("go stop kill eat",:verb)
    update_dict("the in of from at it" , :stop)
    update_dict("door bear princess cabinet",:noun)
  end
  
  def update_dict(str_words,token)
    words=str_words.split()
    for word in words
      @@dict[word]=Pair.new(token,word)
    end

  end
  
  def dict_display()
    puts @@dict
  end
  def scan(sentence)
    sentence=sentence.downcase
    words=sentence.split()
    pair_array= Array.new
    for word in words
      if @@dict.include? word
        pair_array.push(@@dict[word])   
      else
        what=convert_number(word)
        if what=='number'
          pair_array.push(Pair.new(:number,word.to_i))
        else
          pair_array.push(Pair.new(:error,word))
        end   
      end
    end
    pair_array
  end
  
  def convert_number(s)
    if s.to_i.to_s==s
      'number'
    else
      'error'
    end
  end
end


