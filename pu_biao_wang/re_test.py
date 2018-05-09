# -*- coding: utf-8 -*-

"""
正则表达式测试
"""
import re

content = """【处方】大黄100g	炒牵牛子200g
    槟榔100g	人参100g
    朱砂30g
   【制法】以上五味，朱砂水飞成极细粉；其余大黄等四味粉碎成细粉，与上述粉末配研，过筛，混匀，即得。
   【性状]本品为黄棕色至黄褐色的粉末；气微，味微苦、涩。
   【鉴别】（1）取本品，置显微镜下观察：草酸钙簇晶大，直径60～140μm（大黄）。草酸钙簇晶直径20～68μm，棱角锐尖（人参）。种皮栅状细胞淡棕色或棕色，长48～80μm（炒牵牛子）。内胚乳细胞碎片壁较厚，有较多大的类圆形纹孔（槟榔）。不规则细小颗粒暗棕红色，有光泽，边缘暗黑色（朱砂）。
   （2）取本品1.5g，加甲醇25ml，浸渍1小时，滤过，滤液蒸干，残渣加水20ml使溶解，再加盐酸2ml，置水浴中加热30分钟，立即冷却，用乙醚振摇提取2次，每次20ml，合并乙醚液，蒸干，残渣加乙酸乙酯1ml使溶解，作为供试品溶液。另取大黄对照药材0.1g，同法制成对照药材溶液。照薄层色谱法（通则0502）试验，吸取上述两种溶液各1～2μl，分别点于同一硅胶G薄层板上，以石油醚（30～60℃）-甲酸乙酯-甲酸（15：5：1）的上层溶液为展开剂，展开，取出，晾干，在紫外光（365nm）下检视。供试品色谱中，在与对照药材色谱相应的位置上，显相同的五个橙黄色荧光斑点；置氨蒸气中熏后，日光下检视，显相同的红色斑点。
   （3）取本品2.5g，加三氯甲烷40ml，超声处理30分钟，滤过，弃去三氯甲烷液，残渣挥去溶剂，加水饱和的正丁醇50ml，超声处理30分钟，滤过，滤液用三倍量氨试液洗涤，分取正丁醇液，蒸干，残渣加甲醇1ml使溶解，作为供试品溶液。另取人参对照药材1g，同法制成对照药材溶液。再取人参皂苷Rb1对照品、人参皂苷Re对照品、人参皂苷Rf对照品、人参皂苷Rg1对照品，加甲醇制成每1ml各含1mg的混合溶液，作为对照品溶液。照薄层色谱法（通则0502）试验，吸取上述三种溶液各1～3μl，分别点于同一硅胶G薄层板上，以三氯甲烷-甲醇-水（13：7：2）10℃以下放置12小时的下层溶液为展开剂，展开，取出，晾干，喷以10%硫酸乙醇溶液，在105℃加热至斑点显色清晰，日光下检视。供试品色谱中，在与对照药材色谱和对照品色谱相应的位置上，显相同颜色的斑点。
   【检查】应符合散剂项下有关的各项规定（通则0115）。
   【含量测定】大黄   照高效液相色谱法（通则0512）测定。
   色谱条件与系统适用性试验   以十八烷基硅烷键合硅胶为填充剂；以甲醇-0.1%磷酸溶液（80：20）为流动相；检测波长为254nm；柱温为25℃。理论板数按大黄素峰计算应不低于4000。
   对照品溶液的制备   取芦荟大黄素对照品、大黄酸对照品、大黄素对照品、大黄酚对照品、大黄素甲醚对照品适量，精密称定，加甲醇分别制成每1ml中含芦荟大黄素、大黄酸、大黄素、大黄酚各16μg、含大黄素甲醚8μg的混合溶液，摇匀，即得。
   供试品溶液的制备  取本品0.8g，精密称定，置具塞锥形瓶中，精密加入甲醇25ml，称定重量，加热回流1小时，放冷，再称定重量，用甲醇补足减失的重量，摇匀，滤过。精密量取续滤液5ml，置烧瓶中，挥去溶剂，加8%盐酸溶液10ml，超声处理（功率250W，频率40kHz）2分钟，再加三氯甲烷10ml，加热回流1小时，放冷，置分液漏斗中，用少量三氯甲烷洗涤容器，洗液并入分液漏斗中，分取三氯甲烷液，酸液再用三氯甲烷振摇提取3次，每次10ml，合并三氯甲烷液，减压回收溶剂至干，残渣加甲醇适量使溶解，转移至10ml量瓶中，加甲醇至刻度，摇匀，滤过，取续滤液，即得。
   测定法  分别精密吸取对照品溶液与供试品溶液各10μl，注入液相色谱仪，测定，即得。
   本品每袋含大黄以芦荟大黄素（C15H10O5）、大黄酸（C15H8O6）、大黄素（C15H10O5）、大黄酚（C15H10O4）和大黄素甲醚（C16H12O5）的总量计，不得少于3.0mg。
   朱砂   取本品2g，精密称定，置250ml锥形瓶中，加硫酸40ml与硝酸钾6g，缓缓加热使成乳白色，放冷，用水50ml，滴加1%高锰酸钾溶液至显粉红色，再滴加2%硫酸亚铁溶液至粉红色消失后，加硫酸铁铵指示剂2ml，用硫氰酸铵滴定液（0.1mol/L）滴定。每1ml硫氰酸铵滴定液（0.1mol/L）相当于11.63mg的硫化汞（HgS）。
   本品每袋含朱砂以硫化汞（HgS）计，应为55～75mg。
   【功能与主治】消食导滞，祛痰通便。用于脾胃不和、痰食阻滞所致的积滞，症见停食停乳、腹胀便秘、痰盛喘咳。
   【用法与用量】口服。周岁以内一次0.3g，—至三岁一次0.6g，四至六岁一次1g，一日1～2次；或遵医嘱。
   【注意】不宜久服。
   【规格】每袋装1.2g
   【贮藏】密封。【"""
print(content)
pattern = re.compile('【\S*】')
result = pattern.findall(content)
for title in result:
    re_str = title + '[\s\S\w\W]*?【'
    pattern = re.compile(re_str)
    match_obj = pattern.search(content)
    match_str = match_obj.group(0)
    match_str = match_str.replace(title, '').replace('【', '').replace('】', '')
    title = title.replace('【', '')
    title = title.replace('】', '')
    print(title)
    print(match_str)