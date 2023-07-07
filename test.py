import g4f


print(g4f.Provider.Ails.params) # supported args

# Automatic selection of provider

# streamed completion
response = g4f.ChatCompletion.create(model='gpt-3.5-turbo', messages=[
                                     {"role": "user", "content": "Hello world"}], stream=True)

for message in response:
    print(message)

lyrics = """
Translate this Japanese song to English accurately. No need to put references or links.

しまい込んでいた　褪せてしまった願いたちを
引っ張り出してあげようか　燻っているんだ
こんな世界なら　なんてまだ早すぎやしないか
いっそ目を瞑って「せーの」　欲しかった勇気なら
今手にしたんじゃない

まだ頼りなくて　剣は不格好だっていい
一人の夜が怖いなら　探しに出かけよう
ほら　肩を並べてさ　笑い泣き時にはぶつかって
それでも同じ未来を　描いたなら進んで行ける

そんな旅を

流れ星みたいに一瞬で　消えちゃうなんてもったいないや
痛いくらい　派手に光っていたんだから
飛び越えていたんだ一瞬で　丁寧に積み上げた僕らだ
でも必要ないよなきっと　今は小さな勇気一つ

それでいいや


標なんてなくて　いつだって手作りの道だ
点を線に繋げよう　　溢れているんだ
不安なんてないと　ちょっとまだ嘘になっちゃうけど
かき消してしまえ「せーの」　身体は軽くなって

置いてきたのは　生きてきた証で
過去の自分とはもう会えないけど

今を歩んで行ける確かな理由は
そこでしかきっと見つけられなかった

そんな旅を

宇宙(そら)の果てにだって一瞬で　飛んでいけそうな光なんだ
泣けるくらい　世界は広いんだから
飛び越えていたんだ一瞬で　粗く継ぎ接ぎだけど僕らは
止まれそうにはないよなきっと　燃える灯火　掲げたら

照らせるから


どこまで　歩いたんだろう
振り返れば
全てが　鮮やかに浮かんでは
背中を押してくれる

刻んだんだ透明で　手放せない大事な日々だ
呆れるくらい　無謀な僕のストーリー

流れ星みたいに一瞬で　消えちゃうなんてもったいないや
痛いくらい　派手に光っていたんだから
飛び越えていたんだ一瞬で　丁寧に積み上げた僕らだ
無駄なことなんてないよなきっと
過去も未来も　噛みしめて

進めそうだろ"""

# normal response
response = g4f.ChatCompletion.create(model=g4f.Model.gpt_4, messages=[
                                     {"role": "user", "content": lyrics}]) # alterative model setting

print(response)


# Set with provider
response = g4f.ChatCompletion.create(model='gpt-3.5-turbo', provider=g4f.Provider.Forefront, messages=[
                                     {"role": "user", "content": "Hello world"}], stream=True)

for message in response:
    print(message)