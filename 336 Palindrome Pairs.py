from json import dumps
'''
336 Palindrome Pairs
https://leetcode.com/problems/palindrome-pairs/
'''
'''
lls =>
needed: +#sll, sl+, s+, +ll, sll#+
can be: +#lls +#ls, +#s, ll#+, lls#+ 
s =>
needed: +#s, s#+
can be: +#s, s#+
'''
debug = False
def isPalindromic(s):
    r = len(s) - 1
    for i in xrange(len(s)/2):
        if s[i] != s[r-i]:
            return False
    return True

A = ord('`')
class Node(object):
    def __init__(self):
        self.cs = [None]*27
        self.inds = [] # index of word in original array

    def add(self, word, ind):
        this = self
        for w in word:
            k = ord(w) - A
            if this.cs[k] is None:
                this.cs[k] = Node()
            this = this.cs[k]
        this.inds.append(ind)

    def find(self,word):
        this = self
        for w in word:
            k = ord(w) - A
            if this.cs[k] is None:
                return []
            this = this.cs[k]
        return this.inds
'''
'lls' => ['lls`', '`ls', '`s', 'll`', '`lls', 'lls']
's' => ['`s', 's`','s']
'''
def buildTrie(words, palindromeCache):
    '''
    Do 3 things:
    1. Add prefix, suffix to trie
    2. Cache palidromic substrings
    3. Find ''
    '''
    trie = Node()
    emptyIndex = -1
    for i,s in enumerate(words):
        if s == '':
            emptyIndex = i
            continue
        for j in xrange(1,len(s)):
            if isPalindromic(s[:j]):
                trie.add('`'+s[j:], i)
                palindromeCache[i].append(j)
            if isPalindromic(s[j:]):            
                trie.add(s[:j]+'`', i)
                palindromeCache[i].append(-j)
        trie.add('`'+s,i)
        trie.add(s+'`',i)
        trie.add(s,i)
    return trie, emptyIndex

def palindromePairs(words):
    palindromeCache = [[] for _ in range(len(words))]
    trie, emptyIndex = buildTrie(words, palindromeCache)

    # ls = ['a','a`','`a', '`','']
    # for t in ls:
    #     print dumps(trie.find(t))
    # print dumps(palindromeCache)

    res = set()
    for i,s in enumerate(words):
        if s == '': continue;
        for p in palindromeCache[i]:
            if p > 0:
                needed = s[p:][::-1]
                for j in trie.find(needed):
                    if j != i:
                        res.add((j,i))
                        if debug: print s, needed, '(', j, i, ')',words[j], words[i]
            else:
                needed = s[:-p][::-1]
                for j in trie.find(needed):
                    if j != i:
                        res.add((i,j))
                        if debug: print s, needed, '(', i, j, ')',words[i], words[j]

        rev = s[::-1]
        for j in trie.find(rev):
            if j != i:
                res.add((i,j))
                if debug: print s, rev, words[i],words[j]
                res.add((j,i))
                if debug: print s, rev, words[j],words[i]

        right = '`' + rev
        for j in trie.find(right):
            if j != i:
                res.add((i,j))
                if debug: print s, right,words[i],words[j]

        left = rev + '`'
        for j in trie.find(left):
            if j != i:
                res.add((j,i))
                if debug: print left, s,words[j],words[i]

        if emptyIndex != -1:
            res.add((i,emptyIndex))
            res.add((emptyIndex,i))
    return [r for r in res]
        
words = ["bat", "tab", "cat"]
#words = ['a','']
#words = ["ccbabgchcggcf","hjicbfdgfffiejcb","bcbbhgejdghjhiebhif","bg","ccdiacebhfaiaifg","jdi","ffhjie","hdacgbbfdeidgbb","dcedddghagahd","ffga","fhie","aigjghhfaijdfhfjjaj","hdg","hiacdbhbbfc","ejfhcbj","bdddbabad","hbihd","ccgbhchfifa","cjaddfbfcaeciiiiiegj","beihhbbcbhaibehd","adjeajfj","i","ahffeii","jgbidfgb","difebafibjedhbecefdd","bfcabjheceafefba","fi","ac","hebhjghfajdajbc","bhhchageegdj","egcfaidaejj","afchfaffbjifc","cicabighjbbhbihbhab","abj","hbifdhbjgj","b","eddbecfdhgggadh","h","bhgdhgjhggcichide","gihghjaihj","bhcgbi","iihefhhiehacbceb","bfbhhcjegdcaigajeb","fhhbajaccedb","jbfafgdhcjecicjghga","adgcjeadcbffi","ejjiijaichiegaieic","e","fajdcijggdfd","dcbabehhjcjeihiadjj","dbhdjbcibfhjabadijj","bgiggae","bjgbjidbjdiehjd","cibd","bhiffcjfccccfj","bcff","fghajg","hfbhhachebee","hacedjjg","hbfjebhadijf","jagfai","hgfcdedceacg","dhicbbigijihfjajd","eiafjedf","agfdidja","ahfghbdifaijcbj","aiahcgicibgc","diiaafbfiibaichcgd","cahahaafbafd","hhf","bidjgiacbiffecade","fcjafhhgghfeaf","fbahihbb","jdddbeg","djajjfhigihgabdcabf","dehdjbjdb","bgfcbgdfi","ifhdg","cabhjabf","jeccefhfcdeiafdb","cidgggf","bcdihejbdb","aajbbbabcigibcija","beeig","fge","igcaecbgbha","dcgafedfgif","dfgcdbhieaahba","dd","dfjihgeee","fje","jeigcfifddddah","chbajhiegihbha","iajd","djjdggajba","bhdaa","gbhgidhebbhccceb","fghhjh","gfhfcfeii","iiif","cfehecjejfe","aeajeggbageicgefhe","djbhjefigjagabaha","fidi","hhhdhccf","fgfcjbfhbfaeaejbiee","iggigad","aibhcjdbfehiaa","fbbbcdcbbeddhgifjhg","jfdgfdfadhdjjcf","hifhffjgdgbaafdbe","jgfhgbbbjd","egfbhcfhaa","jbfejichj","hhbijjejdeaigjif","fcifcdjdgibfhfjdfabh","jdhafgbdgdcaef","hfeieeaigieegg","adahfhhafb","ehigeh","iadebiegbghbjdiibjf","jijdcaeiijcgbfi","bffdedbedhdeecachb","daafdaahfccafagf","aifdfbeiffigjafj","fbbbae","geiddhc","hcaegijihd","ecdhcbj","dfcjdbeibigjbb","defgeg","dabdjciiafj","af","ibehcjehgcbcfcgfdeh","aijjgcahjjgidjagfcf","aaggjibddhcidehajdjb","hed","jib","j","cdgajccccabdjfij","dggefhahgceaiefbjh","dheaefaa","jcii","hjjbjhhjcbiechfea","feh","if","ag","aggadfd","ad","cihifdje","bbc","eejibacbdddfgiba","bdjhcfdffdfidbac","geccaabbdjhbe","ica","geagfddiggb","fhdfhjcghcidgbdaadae","icbccgdhfh","bfefdgaafiiacfg","jaihibagafjbadebbjfj","ffjbaf","egfjacbeadefae","cgfcahebcajbac","bdejjdhbfeegedeeghb","fhfabcd","gfajigcae","iefdbjiicfbg","bhghihdgdbgdch","aie","cdaggccaaidb","hecjbjiedbiadigihb","jijcj","hbcfajef","hadbiddciibeb","gaahifdejbdfacbfcfh","dibai","gahgdeddcaheigggad","aidd","dej","agai","hdhhjdjic","hbbfc","ccgcajjiggiedjfagjg","igfeggjcfbdbd","hjgbifgg","bcijhifjddaidd","jhedajfigb","fda","hgdigefbfbefihiae","edcijdgegcdfcejcib","cb","fadcheig","jbgefidcageficiggc","ighe","bcaig","chfbjiffhc","ceaa","jdfiigbhhgjidjjbhba","dgiifihaaaiiicaaibi","gcf","eiefiifeba","dibbfaijbh","cefgedfdjdg","jdfdfebaidhciejhfi","idaaabfdj","ijeabgajg","dfeefbdfebac","eehcbaagiha","igedadbgiddedd","bjg","djiagaddgcdhjcj","ecdaigiaceba","ij","gcjfh","iedajagbefa","gjcjhd","fhc","jgjjibfhfehedcdibed","gddd","dhicf","jeifabceecjjbiciiifd","dadjgbfajeigaadidg","aeicgceibechfaabajb","bhgi","ebafjbjdehgjdefjfhj","bjcfcecgeiaahcb","jh","hhfbabiehecdih","hdiiafafagfbfadgbdjj","bieijgcfbj","hafceibjfcdigchcbfd","agdijhjfiggihaeha","eiife","fdjjiiefcbcicde","idahfhgcjhei","iefch","hbfch","ejehfjhjbeeabidcjcf","d","ahgbaicjj","bdcgbhghgfhbehd","dcfcddhfcbgaicaaigie","fciihbjjffeaeibaf","ghfjjffffaie","hijbcia","haca","aeihhebfacfgcbj","haajdeebdafcbe","bf","cdehffhhcibbdjac","fbdcc","ehg","hiieaijgbbhcgadbbe","igbecadcjbfcc","aedaafebeiabfg","icigabibdchhdjheiihj","f","cigdgdaib","gjagi","dejefgaebgaibf","jajgibcjcgdfbjh","gabbdhdbbdjgaebbj","gedeggigbgdbghjch","eeeheahddejijci","cfj","jddbb","chjajaaicda","adeaeccfhaaagag","aabgijhcj","igjbbedi","feeibagjcae","iedigjh","fdhgbdebachdbc","agbdgdhb","ibjhedbabggbhh","cjjf","cidgdggfdhhgjbhih","difhhiehghhe","afjeighacf","cjgcjaicbbeg","fdgahbh","dehbeici","a","egccdjbijhcegibabgb","fdjajhg","gihdifdgdhfaiaa","bebedfcgbja","ehjaebhgibihfcabbeee","gfcfcah","gbaaegfdeafec","dfgcfg","jcfjhgbjcbjgijgfch","ihgjjdgaahbfg","eeaaggggjeahbegc","agcihhgddidfjhcbdg","ijiaic","cfgeechejidadf","iiefj","gaefeahjegehfe","hadhad","hjfedb","beffdhdcbcfgfadfdb","cfbbaddi","gf","gcbecb","abhcbgigjei","efjcg","bdcjbbjfcfdceadjefg","aaciaafbij","bhhbeaifdjfeaiijaec","jdhdbfhhgee","ehfidjgc","dfddbcabajcjbeefg","ghh","djifijij","iaigcjcbdigchhghedg","ddcc","jejjahj","hjifjbaacceejjdihdah","adfbaefhga","cahdhbdagg","adhifjhichjfiaaahb","fegebejefhieecjfa","jfgbhibhhfbjdjdgdg","fjdifb","igjieg","gcjddaebfefgdgddgii","fecjdfbeea","cbja","hecaaejgaiac","cgfgh","cdahac","ge","iafadjffigibi","ggbefa","eeheghaffgbaehbid","hedhbbebdefbj","ibgfbjdgdiedghighaic","igijagai","fdfehiiah","bicdehijdfjhfafe","ecgegfaecfcccbih","fcdbfeejbgcfh","gidbejecbhdffafggedc","higafejifbcdhbd","bfa","ifffagi","gfhjhbadaebefbbccb","edibbjccjhjedej","fcecacdaibidcdidiei","bbifdeaihihgciffdh","feibbeccaag","daij","dhea","ecgbdifaijaghih","bbfaijcchahhjcbgg","cfehbghf","ccecheh","ijdeehbjfbgchjaf","dgeiahfjc","bbcfiegihi","afbaehbfjfihaibdfbc","jjjhabiachcg","bfhfbaebhdccdgafb","bigfhggghi","cbfffieahcabjfejfbd","hcehicbjci","efbhiaah","jjddgj","iejidbadjihgj","idd","jaie","bdfaiceedgcifbdad","diiciighejgba","hjchbcidchei","bgg","bgccegbbibjhigcjd","ffbbbihbdhiefihc","ffiijahhihfjjeebchh","hchjcfegac","acjgc","ddijdhhcbaajjfa","hjfegegg","hebdjhffca","gacbihhdibejihfeb","effihgid","eddhficecaicadgiadg","ccheaecb","dja","hhjfc","dagbgeea","gfifibejffh","ecafchigbecdhbjbjga","ifgjjheegbfab","aegeabfgcbej","cg","gjcfb","c","jaacjhccaic","ajggcdieihgiieiccajc","ig","ggcchafagiie","edffjb","ebchagi","g","ebjhfihhi","efdjhbjgbdb","gfgbjaifdfadfb","gdcfjaaeejjbfgagbef","cjfgaehehbjc"]
words = ["eieeebdjfagghdbfchia","gfdeaccfjhgcgg","gbegjcjjihgjc","jcfdgcgjc","fieihihejjcai","ihgbbec","ejdhiadahjbbfhge","dbhjhgdhi","cbjbdhh","bhijghhaid","ffgfdcficeafibifbih","fijeecbifijjdfddhafi","chgjcbaee","hdjiaiafgaeib","ejbbfdgbc","acbh","efg","aedjdijjeacbajefj","heddcjijfcfcjcije","i","hjiee","idjbdgcchcigchf","dgadifhgfhbcdbbbecc","afjhihijeffj","defffbdgceceefdfcb","eiaeidghdifdbggaggfc","bhhadhfidhha","cgdhjaadgjbde","aiaghjaghigea","hdceeehgga","bgadhjhieff","dicebicahecbi","fedebdihigbaeggd","idbifdghbb","hieid","abjeaa","figjbbebjcahcf","dcdbidbdhdfbbebi","ghfbfbife","bbb","hhdj","hdiai","jjhgch","fjefbdcacijcieii","beeagfhiiccaefe","efbegbcicahjcia","ehjhjgedbijjehged","ehhhdajbjiicfh","edbeeidajii","faicgcafhece","ebgahggfjeajbihcd","bciggiajgjfidhiidj","dfhffebbgcjdda","iafchhgadbid","fagacbadfcbbaf","hjjgbgiefgci","hdedjcigdhjbhgahcab","ehfjibdc","aageeicai","fii","jbdcebjfci","jhbibdbchchdab","jacaiabefihfiagaj","hfjedjfjdgebjichgcj","cdeieijdfeaafg","ggcjcdhchhj","jdi","fj","gbdfhddbahg","fa","cdgcjaai","icheejeehfiedjaa","f","dieeg","hfaibdbjigciadaifcb","cgda","c","bfiddgeabefciahe","ieihahicdeijfjdeie","ihfad","gfiijjcaffeicfea","hgafeaiegjcbihbd","aiedijaa","fafagiiajafdhdh","jhihcbiege","jaghhccheejjce","aiahf","hjicjcahiahcgbhcif","dhggbdcddgegac","jc","ccbhebhcehj","ajhgifcfdcdgfehigd","ajfejeahbgfjib","idigcgbbijfe","hfghgbcjahjghf","eji","ibejcgcfdebhhd","jeeigaiadhh","jhbggbfejef","ahidddbfacddfhjhjgg","dhc","efa","hjbehadfbdeahd","jfead","fhhfehgjc","fgjefeijciahfa","ahgabaebdcdii","gjahd","jfideaaiieigbchgjb","djfigbbifefiffchdd","dggefibheadgije","ch","fijgchjcae","jchgihcfhbf","jhied","ceifjjjaihijhajhfeab","dhfdbdcebbacdg","gdai","gfjcajfb","ihbefhddjfjeefgcicje","chajbecjfgcgbf","bdhgfafafheeb","jjhhgidgcfcaf","habfbc","djfbj","ighgebefcegacach","hejdgig","faeejcjgciid","feccehbfacaecbhbgbc","j","hceaa","jbgibjjccbjbjediacda","igdfhjefcjg","adh","addfafaiafceddbbbb","ihjjjhhbig","ebbabghcb","aceiehheccahhjgcjc","edgjjch","ddhbecdgdddhfejbbcai","dfjbiiedeedgiigf","he","jbachifbif","cacgabgghdhhhgbdf","d","gcahejiec","ihajcbg","jjiib","hideihacfhbh","dhbihjchhj","eaididibhbgcaabifhi","chfb","dje","b","beaehdcffj","afjijfaggg","hb","dgcgadfafifh","eihdhhch","faehddchdgahifb","baahieaiddefhh","eedgaejjbhcebbgiih","becbaad","giafhieb","cijjh","efigdfgdh","ffgfbgfiabijhc","aafdcfcjecbebfib","faffejbjhedfibfhf","fd","gjhbi","geeifjbfje","jbghifihabhb","gehffffgicfjaed","ddejhffad","acbfbehgcdjcgidfgj","hbacf","ece","hfabihdhgggjjcgja","hibdjbgdbadeiajchd","aghgafejegcchidide","ddcebfbgihcbjegefj","eahhhbabedgi","jbjcifjhieg","fdfgfaieejh","bfhchaghjjchba","ehiae","heifahghjciahhdh","ig","ihc","hccjcjaiiaa","hdhefbgefjadbiiacf","gajgcjhadd","gfce","eaegbfjeihfebjj","fjjdeicbda","efbbeijgceiiee","ahbjebae","ffa","gjdfijghgdfb","hfgagdbbghcejh","afajbechh","cicigfdbfjccdccegf","ffhdiifadbjdjijc","hdggdjajb","ebdia","gfdjhbj","bgdfc","dfceagabfecbcjbhb","aheeifgiibjigh","ifgdaidba","ciadjfjhd","eggadicdec","g","cheiafaehiefcb","dhhhebhicffiecbehb","ahfhjhfideafc","befcacfeddaiegeghff","bgahbgaibdhbdddje","eedghcafgcfhebdehead","igjgadicjdgbhhbheh","gaecj","iceieaiigb","bdjfhihgafjhcb","jge","ic","dciehedicbaee","fhcfjfdcggbhagea","ecidjgffggbcejecigg","jabi","cficjchbefd","dgcdhhebgfhbgbdca","eeabbfaibdedhfdc","giaicjie","hhfejfgfcbd","bfeccfjgeifjhigdgdhg","cjhjjbchh","cehddjbjbdheaaj","iijj","eciigagdaf","fb","eae","gbegd","dcgecabdgjabe","dd","ddiceefed","fehadhcfbafhfjficj","cfgdihcfa","fcgejba","chchdaeaii","ijfjhjaii","accaeheabiceijhadh","bdad","jgcjaed","bccbejd","ha","cbjjf","cgh","fjfcdfbdhdfbhhb","afi","hcdh","hdchiedjahdh","hcdhbjibhgachcjiiihj","ahjdjgfegafihaaijgfi","daceabdecijcch","ejgdaecjjcbhcbifhea","je","gafihfgbibijdhejadbg","fgbdafddifcgjbecij","fbhhebh","ffbijihbg","hjdfdijaaai","eajaidbjejbai","edfgfhehjdeegba","fjdjjcaidcjegi","beeijibhdfbfiig","hfddejcb","eaaiefha","haifdfjgeiidehad","ddagad","cadfejdfdeijb","hhebgbh","cefid","idgiaebjdcdijg","bjiddgdcfbiddbd","jfgdabdaid","dibfefcdcgdacihfe","fhghhfjjagifadagahgd","jecjjcchjfiaj","eggeiehaeggbdcgdebia","dfh","djdhbdgcgcjjgagdjdib","ddeigbigbjajjdcbiah","bgbaeea","daedcccfaejiiijceeac","heiegcgadageidgfida","ibgeh","cghejcedbbfba","ebfbchddcjhdhhh","dgeejicfdadhhfj","eaahddh","fhaddbaeggcgehf","eebiahbbhfjbba","ifh","ahi","ijigjdhc","hhjcceihjidjhbjab","abghce","ei","fjcbh","gec","aecaecaaicfgddfdjage","gdfgdh","abbijffichbcfadgjgc","ddccjfbedaih","biecdabhih","dhaejgaiecaefdbb","eeccjffjgag","ci","gca","aghhjah","hdfedgjgjicg","djebdhcfehbcgd","fidaefbfffd","dajadgbabheejaf","degeciccaeij","hghfdcadfgaaaaebacj","jidicafdjgchcjeaddg","bhjchgbj","jajb","cjahfgachghdajbjai","igahibghbiejjeeche","dcijchgabhajaijga","biecej","gedfdbhfci","ddjcfahiahcdaijbeh","da","gcehj","bjaedeiedcbf","jjjbacbiigej","jafejfdjeijdhfhacia","afjjhbdfcajdeege","cgj","gjjgiaefefhjhabaad","hfj","hgaajeajeihhbdcfb","gjagdfeffffjg","bfbbbgic","ddjahjeihcgcebec","ijacdhjbhfgggi","jjbjifjfib","jii","adfjeeihgfcdcacfff","ejid","hehcbjhijcddbhc","ehcbjadi","cdbcjiiaaedid","a","jhhajf","eccgjigajcadcdijjhhg","hebcbichdiffdje","ef","cjcjjcigagdeiahaigh","bjeahjeddjgcfbhabde","gjaijjcibaia","hcghdghaba","chadficjhd","ebfbbjgjbehdh","gdhfeijiedh","bgecgf","hcfc","ajbhaehij","idj","gjeafabahabacehhadj","didggidbefag","bbeijgcif","fg","dhheeeiaai","gi","ccbbhjeechjgdbdjgeg","cgdeagc","bjaegifjejdiac","ehebihifehagdcfgd","fgdfgiedgchbffebe","acea","ifhccjhjjdcdcdd","eafabdccg","bciafbaddbiajcfaba","dibhadicbedaedcf","icbjcbgdjcbbbihciac","dchhfaaedgjc","jdid","cgfiecbfhgcdih","acgiahceegjij","gcjibifagcbfcaf","cdejbddbcfggh","eegadhiggd","jhfeihihiggheaeh","eaegfhjigghh","dgdhjdhdfccgjed","dgcdafhggedgihd","hahbghccdjfdaicgjh","dgiedc","cgefaigdahja","geeibedddejiid","hhcbgcddeghjjhahad","ajcfegjdfej","bciefcehjdgacfhiabhb","bejddfchf","icgfihjcfdjbjihgfdf","hfcge","ggici","aiheciafhdij","dggdgadjbeahcbbed","edeeijcbijaaf","jd","hjbe","bafdhehigef","cfiiabjighdgcb","bfegji","aahgcfcfgaafaej","ebeab","cibceag","gbfffdgahjcgb","gdheadhf","h","ebhjjeig","hccacaabheehaeedg","jcag","bddgb","acbfbj","fcgjjhgedgghgc","gchhehadhbdjj","dabah","jeigdbiajiffdcc","af","bhdcce","hcgjjhaajdbbibiaaaef","ghfhgcgjbjhjjaha","ejdegcbfadeefcdg","ddefc","ibhhjebfhfjbgjhafdhg","jhgfbadac","gjiehddfhcjf","ahghjbhdhbgg","ifjeeicjdbbdhge","digei","ibdiafghbegcbd","efjf","fbhgidbjbaacb","hhgccfbi","egiigbaebeh","ifcabgiiie","cee","haejehfabheechj","gchheebifi","dfjjggidicbhgace","ifgaaghfjfbbhaacibj","ibcjhfa","hgajachehijbdbgfh","bgcbbahjgfae","fgadbhhhdfheecace","gacjedibfbhdbcfb","bdgggg","cid","hichc","dgjc","decchcfcfjb","fhaidcii","ja","ijdgiiajbe","hi","efgicgddfhdfied","hjafceb","ajdhjgjeie","caiechgjegegbdbee","dffiaefbefagie","affa","bbcaeffbhefdcfghedab","gjbe","gegfhhiihhfccbba","igcgj","efhbjcfdfdghiebgbbaf","fghddheejjcbadg","ceieiafeacj","acbcdjfejdbgcg","heheffbjagegig","bbecfgjdcfcahj","faebeadiejiheejij","ceijidbiagehh","jfehbijha","iejdiid","gedd","deejaicjcdbaj","hbcjhce","ahfjbe","jjdifbjfcjbb","iihebei","jjbdbjihghifijc","fhcjjifccdddh","jgbahb","deiifabadjadah","eajajijdheggbdjbfcdj","ijdgadceffag","edd","fi","eahfjiidebg","acajeahddji","fdhafdggcggiffbc","diigjihdebabiffcef","jdiiibbhii","chcgcfgcjj","iahicjfcjdddgjjjghi","dffcghijfehfhg","abgjbchcfijg","ddafiadhhciejhbehegi","bheic","jaigbfbbffhcjfddeab","dhcjhigjfdbfged","bifhfc","hgegfgfc","addjfi","iababijcfcbdb","ibgfiba","fgdjaejcfjibdg","jdhjfebjgbda","dehfaegigafcg","cdfbdjgfiggibechejgc","e","diccheec","ggd","aj","hjagfeehafec","agfbcdijdaca","cgcifccjbeegb","fji","dbfejghagca","iicehgdigjb","aiadaaagfbf","diidbddgjjhbfj","cidfigaefbbibdcgbig","ibfegcajcegidc","cehaibgccejieeceebgf","fiacaieiegagf","aijjhfdg","fbgjeheb","chciicbeebedbfgabe","iceicaiiccghgjf","bdfgecag","ejeicfihjcfdabge","dbd","ffie","dhee","jjefdfghaibfegbcbjii","dabbbcf","gfcjaibgiadh","cjcaahi","gddhaeehaafidf","aigbgddib","bdddfaedfcfbb","cifbf","efdibhebc","cfijhghb","fjiibjacegiac","jhijbejahbidcgg","dbjfbgfgdageia","eibbdegdciad","gjh","eddihjjfefee","dbgcjdfedjgacfafai"]
palindromeCache = [[] for _ in range(len(words))]
print dumps(palindromePairs(words))
