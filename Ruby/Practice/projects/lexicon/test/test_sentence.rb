require "test/unit"
require_relative '../lib/sentence'
require_relative '../lib/lexicon'
include Parser
class SentenceTests < Test::Unit::TestCase
    @@lexicon = Lexicon.new()
    Pair = Lexicon::Pair

    def test_subject()
        sentence="kill the bear"
        got_sentence=Parser.parse_sentence(@@lexicon.scan(sentence))
        #assert_equal(got_sentence::verb,"kill")
        puts @@lexicon.scan(sentence)
        assert_equal(got_sentence,Sentence.new(Pair.new(:noun,"player"),
        Pair.new(:verb,"kill"),Pair.new(:noun,"bear")))
        
    end
end
