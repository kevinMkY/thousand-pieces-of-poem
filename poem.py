# -*- coding:utf-8 -*-

from itertools import count
from random import randrange


def progcess(res, words4, keystring):

    num2 = len(words4)
    # check
    if num2 == 0 or keystring == '':
        return ''

    count = 0
    while res.find(keystring) != -1:
        word = ''
        while res.find(word) != -1:
            word = words4[randrange(num2)]
        res = res.replace(keystring, word, 1)
        count += 1
        if count > 1000:
            print('error : cycle')
            break
    return res


def generalSytx(repeatCount, sytx1, words4, words2):

    print('\n')

    for i in range(repeatCount):
        res = sytx1[randrange(len(sytx1))]
        res = progcess(res, words4, '4444')
        res = progcess(res, words2, '22')
        print(res)

    print('\n')


def main():
    words2 = ['朱砂', '天下', '杀伐', '人家', '韶华', '风华', '繁华', '血染', '墨染', '白衣', '素衣', '嫁衣', '倾城', '孤城', '空城', '旧城', '旧人', '伊人', '心疼', '春风', '古琴', '无情', '迷离', '奈何', '断弦', '焚尽', '散乱',
              '陌路', '乱世', '笑靥', '浅笑', '明眸', '轻叹', '烟火', '一生', '三生', '浮生', '桃花', '梨花', '落花', '烟花', '离殇', '情殇', '爱殇', '剑殇', '灼伤', '仓皇', '匆忙', '陌上', '清商', '焚香', '墨香', '微凉', '断肠',
              '痴狂', '凄凉', '黄梁', '未央', '成双', '无恙', '虚妄', '凝霜', '洛阳', '长安', '江南', '忘川', '千年', '纸伞', '烟雨', '回眸', '公子', '红尘', '红颜', '红衣', '红豆', '红线', '青丝', '青史', '青冢', '白发', '白首',
              '白骨', '黄土', '黄泉', '碧落', '紫陌', '情深', '缘浅', '情深', '不寿', '夕颜', '秋恋', '蝉羽', '浴兰', '沉鱼', '落雁', '闭月', '羞花', '幽然', '静微', '艺雅', '卉馨', '轩然', '子茹', '萦绕', '流萤', '静谧', '流凨',
              '羽翼', '蔓延', '浅唱', '轻盈', '清芳', '黯淡', '纯洁', '涤荡', '皓月', '思琪', '绚烂', '郁葱', '寂寞', '尘世']

    words4 = ['莫失莫忘', '阴阳相隔', '如花美眷', '似水流年', '眉目如画', '曲终人散', '繁华落尽', '不诉离殇', '一世长安', '冷香摄魂', '白雪莹莹', '柳色青青', '拂氤袅袅', '一缕相思', '几分惆怅', '月透西窗', '竹影透窗', '梅影透窗', '浮云沧海', '诗心蝶梦',
              '叶落花残', '弱柳轻飘', '菊韵枫情', '娟娟如玉', '素心凝恨', '几度流光', '幽情难逍', '半卷珠帘', '枝繁叶茂', '拍遍栏杆', '梦回枕畔', '往事如烟', '如烟往事', '梅蕊红艳', '雪抱梅枝', '一曲轻歌', '酒豪诗兴', '树影缠绵', '疏影摇娄', '骨自清奇', '月钩斜挂', '一叶孤舟',
              '半江寂寞', '香消漏尽', '月色锁窗', '万种柔情', '柔情万种', '压酒双流', '唐诗元曲', '唐风宋雨', '惆伥迷酣', '对夜无眠', '唐词宋律', '疏星点点', '烟锁青山', '愁思悠悠', '无言尽诉', '洋洋漫卷', '冷风欺单', '风舞霓裳', '芳菲四月', '一笺小字', '枕上无心', '飞花入梦',
              '一缕芳魂', '梦里清山', '翠柳笼烟', '水嗳鱼跃', '东方神韵', '相对无言', '刀剑悲吟', '猎措旌旗', '芙蓉粉面', '翠色罗裙', '诗心缱绻', '红尘百载', '碧水柔沙', '风曳诗情', '月影娉婷', '一卷闲诗', '花开并蒂', '鹏击万里', '千丝淡馆', '绫罗小扇', '长笛犹闻', '浓雪清梅',
              '流水托明', '把盏清风', '桃源美酒', '梦里神游', '曲终人散', '经火历练', '耳畔呢喃', '闻笛折柳', '菡萏浮波', '幻梦千番', '酿酒拾芳', '碧水蓝天', '清风醉月', '雾锁峰岚', '雾锁江天', '迷蒙隐现', '晓月一弯', '清风携韵', '香柔落笺', '情思缱绻', '一醉红尘', '霎那芳华',
              '月上稍头', '瘳落红尘', '月上西楼', '清音妙曲', '长堤独钓', '千载悲歌', '和墨飞诗', '幻梦三千', '烟波浩渺', '汀花锦簇', '浮云一纸', '锦梦千舟', '益友良朋', '词真句美', '扯下白云', '朝霞晚露', '随心遣笔', '落墨相思', '泪锁离情', '心魂苦荡', '思结幻渺', '满院花香',
              '风亲扬柳', '夜雨敲窗', '长堤漫步', '雨卷飞花', '冷雨敲窗', '飞花逐韵', '万里云峰', '雅致清新', '茫茫情海', '幻彩烟霞', '逐花刻叶', '芳颜赴梦', '日影疏帘', '燕舞莺歌', '梅蕊馨香', '月眠湖水', '笔点梅红', '尘梦欣欣', '美影梳风', '蝶开羽翼', '新月如钩', '红袖添香',
              '梦中彩鸢', '紫陌繁花', '藤盘叶绕', '祥云瑞彩', '雨洗岑山', '风送飞花', '浮舟碧水', '勾来幽恨', '冷月清辉', '窗弦凝明', '落花追梦', '月皓星稀', '竹影攀窗', '清风挽竹', '点点流莹', '渔火摇波', '魂断玉碎', '一梦轩辕', '几度轮回', '风铃载梦', '欲点诗香', '幽丝漫洒',
              '凄然细雨', '玉面含羞', '梦心成蝶', '樨柳苏晴', '故溪歇雨', '虚阁笼云', '小帘通月', '蝉碧勾花', '雁红攒月', '落叶霞翻', '败窗风咽', '风泊渡惊', '露零秋冷', '花匝么弦', '象奁双陆', '珠蹙花舆', '翠翻莲额', '汗粉难融', '袖香新愈', '种石生云', '移花带月', '断浦沉云',
              '空山挂雨', '画里移舟', '诗边就梦', '砚冻凝花', '香寒散雾', '系马桥空', '移舟岸易', '疏绮笼寒', '浅云栖月', '香茸沾袖', '粉甲留痕', '就船换酒', '随地攀花', '池面冰胶', '墙腰雪老', '调雨为酥', '催冰作水', '做冷欺花', '将烟困柳', '巧剪兰心', '偷粘草甲', '罗袖分香',
              '翠绡封泪', '枕覃邀凉', '琴书换日', '薄袖禁寒', '轻妆媚晚', '倒苇沙闲', '枯兰洲冷', '绿芰擎霜', '黄花招雨', '紫曲迷香', '绿窗梦月', '暗雨敲花', '柔风过柳', '霜杵敲寒', '风灯摇梦', '盘丝击腕', '巧篆垂簪', '翠叶垂香', '玉容消酒', '金谷移春', '玉壶贮暖', '拥石池台',
              '约花栏槛', '问月赊晴', '凭春买夜', '醉墨题香', '闲箫弄玉', '修竹凝妆', '垂杨系马', '帆落回潮', '人归故国', '小雨分江', '断云笼口', '烟横山腹', '雁点秋容', '问竹平安', '点花番次', '一曲骊歌', '一盏冷月', '笔墨乱星', '山高水深', '柳枝冷依', '云雾飘摇', '落叶萧萧',
              '凤凰凝雨', '世态炎凉', '缘起缘灭', '梦落黄泉', '水声滔滔', '思画不减', '古筝轩音', '十指轻铉', '手捧花蕾', '满城黄沙', '半边冷寒', '柔水情深', '一粟凤夙', '柳树依风', '揉碎光阴', '轻盈诗香', '梦回故里', '醉生梦死', '方田娉婷', '旧梦残烛', '涧籁潺潺', '竹林深冷',
              '空山无人', '清风拂影', '望穿秋水', '满心牵绊', '一杯清酒', '抚琴千首', '遥望苍穹', '墨花星章', '断晴悲凉', '秋水更明', '流霞染笔', '笔墨卿奏', '蝶语冰冰', '残花碎晓', '眉目秋锁', '泪染红尘', '斗转星移', '长风万里', '呼啸苍茫', '织梦行云', '婉约风华', '乱雨鸣笛',
              '山外青山', '摘星揽月', '冷舞清愁', '醉生梦死', '借酒消愁', '知音难寻', '梦落断桥', '陨落苍凉', '苍穹婉歌', '花影怅怅', '落花惊梦', '舞字撩曲', '凝露散香', '寒风习习', '一纸狂澜', '梅花开曲', '粉黛柔琴', '暮云幽幽', '粉珠滢渟', '暮雪残更', '叶落萧萧', '苦莲雨芯',
              '花香无暖', '翡翠怜红', '星月随唱', '一抹红颜', '尺枕无眠', '一叶渔舟', '狼烟十里', '地动山摇', '红花绿叶', '帘外星稀', '万家灯火', '推窗半醒', '柳眉凤眼', '粉面含春', '算尽机关', '绿柳舒眉', '红梅含笑', '桃花碎瓣', '一瓢清墨', '寒风月下', '一往情深', '空留一梦',
              '冷言冰语', '幽幽水月', '枫叶红染', '世态炎凉', '十指轻铉', '云花奏墨', '翩翩起舞', '笔墨卿奏', '蝶语冰冰', '残花碎晓', '眉目秋锁', '泪染红尘', '清风徐徐', '吟尽秋寒', '山外青山', '碧水荷塘', '龙舟响鼓', '暮云幽幽', '高山流水', '摘星揽月', '冷舞清愁', '靓女香颜',
              '苍穹婉歌', '绿叶层层', '揽秀群峦', '招新吐故', '幽径蜿蜒', '疏篱青圃', '翠柏青枝', '银装素裹', '微波倒影', '香波浮动', '杨柳枝头', '紫日熏风', '碧空如洗', '燕子穿堂', '笔挽风云', '光明磊落', '书情墨趣', '夏莲妩媚', '春雨缠绵', '夏莲妩媚', '冬梅展蕊', '踏浪高歌',
              '泥松溃蚁', '湍急溯阻', '万象江湖', '时光转瞬', '宋韵唐风', '携手同把', '青山绿水', '绿叶层层', '一年四季', '招新吐故', '揽秀群峦', '欢歌劲舞', '翻江倒海', '百载强权', '诗祖昂头', '战战兢兢', '漂漂涤涤', '如驹过隙', '软若温柔', '风清月朗', '醉生梦死', '借酒消愁',
              '难醉红颜', '花影怅怅', '落花惊梦', '舞字撩曲', '凝露散香', '星光柔漫', '闪烁思念', '一纸狂澜', '梅花开曲', '翡翠怜红', '一纸鸿文', '星月随唱', '一抹红颜', '人影郁郁', '苦莲雨芯', '花香无暖', '綺梦空兮', '望穿秋水', '寒风习习', '云雾飘摇', '叶落萧萧', '暮雪残更',
              '叶落萧萧', '粉黛柔琴', '月映寒窗']

    sytx1 = ['22,22,22了22', '4444,4444,不过是一场4444', '你说4444,我说4444,最后不过4444',
             '22,22,许我一场4444', '你说4444,4444,后来4444,4444', '4444,4444,终不敌4444']

    generalSytx(2, sytx1, words4, words2)


main()
