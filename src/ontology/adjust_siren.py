#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

foodon_lookup = {}
siren_lookup = {}

nameless = '03301032 03301034 03301067 03301068 03301076 03301078 03301107 03301131 03301149 03301152 03301160 03301163 03301168 03301173 03301183 03301192 03301199 03301206 03301212 03301213 03301221 03301229 03301253 03301287 03301288 03301305 03301308 03301309 03301323 03301324 03301332 03301350 03301378 03301398 03301410 03301412 03301418 03301436 03301437 03301467 03301511 03301524 03301554 03301563 03301575 03301587 03301600 03301614 03301626 03301627 03301649 03301670 03301740 03301744 03301753 03301754 03301757 03301772 03301824 03301825 03301840 03301849 03301867 03301908 03301909 03301913 03301928 03301932 03301947 03301962 03301971 03302034 03302035 03302047 03302061 03302067 03302069 03302071 03302081 03302105 03302121 03302122 03302123 03302143 03302147 03302170 03302187 03302190 03302210 03302218 03302219 03302228 03302243 03302274 03302291 03302384 03302386 03302404 03302406 03302408 03302416 03302420 03302425 03302454 03302456 03302467 03302477 03302513 03302518 03302532 03302548 03302566 03302573 03302574 03302577 03302596 03302620 03302630 03302652 03302657 03302671 03302703 03302726 03302780 03302787 03302805 03302881 03302927 03302935 03302948 03302954 03302987 03302988 03302997 03303050 03303062 03303076 03303079 03303095 03303098 03303100 03303152 03303159 03303175 03303179 03303186 03303213 03303216 03303347 03303361 03303363 03303377 03303390 03303395 03303397 03303398 03303400 03303415 03303511 03303554 03303707 03303763 03303770 03303826 03303830 03303843 03303885 03303894 03303919 03303921 03303930 03303938 03303946 03303951 03304000 03304005 03304006 03304018 03304034 03304035 03304041 03304065 03304076 03304077 03304084 03304091 03304099 03304104 03304110 03304152 03304153 03304173 03304198 03304202 03304206 03304231 03304233 03304243 03304244 03304256 03304257 03304259 03304293 03304338 03304339 03304372 03304373 03304442 03304443 03304448 03304464 03304495 03304497 03304502 03304538 03304539 03304547 03304561 03304570 03304571 03304596 03304599 03304603 03304607 03304628 03304637 03304641 03304642 03304650 03304660 03304674 03304688 03304693 03304699 03304707 03304750 03304766 03304814 03304820 03304829 03304831 03304835 03304839 03304851 03304854 03304862 03304865 03304870 03304873 03304877 03304879 03304881 03304886 03304888 03304900 03304902 03304912 03304913 03304928 03304944 03304946 03304953 03304957 03304960 03304996 03305013 03305015 03305034 03305063 03305067 03305086 03305100 03305126 03305128 03305165 03305168 03305191 03305223 03305231 03305238 03305285 03305286 03305318 03305319 03305334 03305367 03305368 03305386 03305393 03305433 03305445 03305452 03305455 03305495 03305510 03305518 03305538 03305557 03305564 03305595 03305605 03305618 03305629 03305691 03305708 03305714 03305746 03305749 03305754 03305757 03305772 03305782 03305797 03305804 03305819 03305850 03305862 03305869 03305874 03305987 03305991 03306008 03306016 03306026 03306056 03306076 03306082 03306109 03306113 03306126 03306129 03306131 03306133 03306140 03306141 03306150 03306158 03306163 03306165 03306177 03306181 03306188 03306191 03306208 03306220 03306233 03306239 03306247 03306261 03306274 03306308 03306324 03306325 03306329 03306351 03306352 03306361 03306362 03306372 03306375 03306391 03306393 03306395 03306400 03306411 03306420 03306451 03306457 03306458 03306460 03306461 03306463 03306465 03306475 03306476 03306477 03306487 03306506 03306515 03306521 03306529 03306534 03306535 03306537 03306541 03306542 03306547 03306548 03306553 03306566 03306601 03306638 03306645 03306649 03306652 03306653 03306686 03306694 03306698 03306714 03306729 03306740 03306743 03306755 03306759 03306767 03306770 03306802 03306822 03306835 03306841 03306846 03306891 03306916 03306936 03306953 03306996 03306997 03307019 03307072 03307094 03307161 03307167 03307179 03307184 03307188 03307197 03307213 03307218 03307221 03307232 03307244 03307273 03307281 03307306 03307308 03307311 03307336 03307338 03307340 03307343 03307349 03307370 03307376 03307397 03307398 03307399 03307432 03307474 03307501 03307543 03307552 03307580 03307607 03307609 03307638 03307643 03307657 03307673 03307688 03307690 03307710 03307716 03307722 03307727 03307728 03307744 03307747 03307767 03307770 03307771 03307781 03307787 03307821 03307847 03307862 03307865 03307870 03307873 03307924 03307931 03307986 03307987 03307996 03307997 03307999 03308000 03308007 03308012 03308014 03308019 03308022 03308023 03308029 03308031 03308032 03308050 03308057 03308070 03308084 03308090 03308093 03308094 03308107 03308108 03308120 03308121 03308146 03308149 03308151 03308164 03308171 03308172 03308173 03308176 03308177 03308183 03308185 03308188 03308197 03308198 03308200 03308205 03308216 03308217 03308227 03308228 03308230 03308232 03308256 03308262 03308263 03308274 03308275 03308276 03308283 03308289 03308291 03308292 03308324 03308332 03308338 03308366 03308368 03308378 03308387 03308420 03308422 03308427 03308428 03308429 03308430 03308431 03308433 03308442 03308444 03308447 03308451 03308452 03308459 03308465 03308493 03308494 03308499 03308514 03308518 03308540 03308552 03308556 03308559 03308575 03308582 03308583 03308585 03308587 03308593 03308609 03308619 03308624 03308644 03308649 03308689 03308691 03308700 03308735 03308758 03308759 03308775 03308777 03308785 03308787 03308789 03308792 03308796 03308804 03308833 03308837 03308841 03308842 03308844 03308858 03308870 03308871 03308873 03308880 03308883 03308887 03308895 03308897 03308902 03308904 03308905 03308911 03308913 03308919 03308939 03308952 03308955 03308956 03308960 03308967 03308971 03308972 03308976 03308977 03308979 03308980 03308982 03308983 03308984 03308985 03308987 03308988 03308989 03308990 03308992 03308998 03309000 03309002 03309019 03309056 03309058 03309062 03309069 03309070 03309084 03309093 03309110 03309112 03309113 03309114 03309117 03309118 03309120 03309133 03309141 03309148 03309155 03309156 03309161 03309162 03309163 03309166 03309167 03309170 03309172 03309174 03309177 03309178 03309180 03309182 03309184 03309186 03309190 03309191 03309193 03309200 03309201 03309202 03309206 03309211 03309213 03309215 03309234 03309235 03309238 03309245 03309257 03309259 03309260 03309261 03309264 03309266 03309267 03309268 03309269 03309272 03309273 03309275 03309276 03309281 03309288 03309293 03309298 03309306 03309309 03309322 03309327 03309334 03309339 03309342 03309355 03309424 03309430 03309431 03309432 03309433 03309435 03309438 03309449 03309463 03309465 03309466 03309467 03309471 03309472 03309473 03309479 03309486 03309487 03309493 03309494 03309501 03309516 03309519 03309520 03309528 03309530 03309532 03309568 03309574 03309583 03309584 03309616 03309617 03309629 03309630 03309633 03309640 03309642 03309645 03309655 03309685 03309686 03309692 03309693 03309697 03309705 03309706 03309710 03309713 03309716 03309717 03309719 03309720 03309721 03309722 03309726 03309727 03309728 03309729 03309731 03309747 03309749 03309752 03309753 03309754 03309756 03309761 03309784 03309864 03309865 03309877 03309898 03309900 03309901 03309910 03309911 03309913 03309914 03309916 03309919 03309926 03309936 03309953 03309968 03309975 03309979 03309980 03309985 03309988 03310027 03310028 03310035 03310036 03310040 03310043 03310046 03310048 03310055 03310068 03310076 03310079 03310080 03310085 03310094 03310095 03310104 03310115 03310119 03310120 03310121 03310122 03310123 03310136 03310141 03310142 03310148 03310158 03310159 03310170 03310175 03310180 03310181 03310183 03310193 03310199 03310203 03310217 03310218 03310229 03310230 03310233 03310236 03310237 03310252 03310267 03310271 03310281 03310298 03310299 03310300 03310303 03310322 03310342 03310346 03310354 03310357 03310377 03310384 03310413 03310419 03310425 03310428 03310441 03310449 03310450 03310451 03310465 03310487 03310493 03310545 03310550 03310552 03310556 03310562 03310570 03310573 03310622 03310629 03310658 03310682 03310697 03310721 03310730 03310731 03310732 03310733 03310739 03310747 03310799 03310821 03310823 03310830 03310832 03310849 03310858 03310864 03310866 03310872 03310876 03310877 03310893 03310896 03310903 03310925 03310928 03310942 03310943 03310967 03310980 03311000 03311008 03311025 03311031 03311047 03311048 03311049 03311055 03311103 03311104 03311117 03311135 03311144 03311161 03311222 03311257 03311266 03311267 03311273 03311278 03311281 03311286 03311291 03311303 03311340 03311347 03311348 03311356 03311374 03311380 03311386 03311392 03311405 03311421 03311437 03311438 03311439 03311440 03311457 03311464 03311471 03311478 03311479 03311481 03311491 03311492 03311502 03311503 03311529 03311535 03311553 03311558 03311566 03311576 03311577 03311599 03311603 03311619 03311641 03311651 03311656 03311671 03311672 03311725 03311748 03311752 03311757 03311758 03311759 03311763 03311767 03311768 03311773 03311780 03311790 03311800 03311837 03311839 03311848 03311857 03311859 03311860 03311867 03311870 03311872 03311886 03312038 03312063 03312067 03315054 03315087 03315099 03315135 03315223 03315252 03315282 03315292 03315296 03315315 03315331 03315342 03315351 03315356 03315361 03315427 03315451 03315473 03315477 03315494 03315518 03315553 03315574 03315643 03315730 03315754 03315844 03315864 03315867 03315870 03315888 03315906 03315971 03315972 03315973 03316008 03316018 03316095 03316101 03316107 03316142 03316144 03316145 03316183 03316203 03316217 03316232 03316264 03316277 03316297 03316327 03316330 03316331 03316343 03316370 03316374 03316383 03316389 03316405 03316417 03316423 03316427 03316482 03316510 03316516 03316520 03316535 03316542 03316551 03316570 03316614 03316635 03316687 03316688 03316696 03316741 03316752 03316783 03316860 03316863 03316901 03316971 03316992 03317053 03317058 03317069 03317145 03317146 03317238 03317327 03317332 03317370 03317389 03317453 03317470 03317472 03317475 03317494 03317508 03317548 03317557 03317584 03317621 03317636 03317644 03317654 03317663 03317675 03411028 03411105 03411207 03411246 03411321 03411424 03411526 03411605 03411613 03411619 03411631 03411779 03411847 03411953 03412245 03412282 03460122 03460124 03460143 03460147 03460153 03460163 03460171 03460184 03460185 03460186 03460191 03460205 03460210 03460212 03460260 03460279 03460282 03460296 03460297 03460302 03460309 03460318 03460333 03460338 03460340 03460341 03460342 03460345 03460362 03460380 03460390 03480004 03490004 03530003'.split(' ')

# Read dictionary
regquote = re.compile(r'".+')
with open('foodon-labels.tsv', "r") as lookup_handle:
	for line in lookup_handle:
		URL, label = line.strip().split('\t')
		#<http://purl.obolibrary.org/obo/FOODON_03304344>	"tempura batter"@en
		#<http://www.ebi.ac.uk/ancestro/ancestro_0309>
		#URL = URL.replace('<http://purl.obolibrary.org/obo/','')
		URL = URL[1:-1] # chop < and >
		label = label[1:]
		print URL, re.sub(regquote,'',label)
		foodon_lookup[URL] = re.sub(regquote,'',label) # chop everything from remaining quote onwards


with open('imports/siren_labels.txt', "r") as lookup_handle:
	for line in lookup_handle:
		(id, label) = line.strip().split('\t')
		siren_lookup[id] = label


with (open('imports/siren_augment.owl.old', 'w')) as output_handle:

	with open('imports/siren_augment.owl', "r") as ins:

		for line in ins:
			# this substitutes line's URI reference with textual value
			if line[0] == '*': # and not "' (" in line:
				terms = re.split('(http:\/\/[a-z.]+\/[a-z]+\/[A-Za-z]+_[0-9]+)', line)
				if len(terms) == 3:
					if terms[1] in foodon_lookup:
						label = foodon_lookup[terms[1]].replace('<','&lt;').replace('>','&gt;')
						terms[1] = "'" + label + "' (" + terms[1] + ")"
						# print 'textualizing' , terms[1]
					else:
						print 'couldnt find description foodon_lookup :', terms[1]
				line = ''.join(terms)



			if line[0:14] == '    <owl:Class':
				terms = re.split('([0-9]+)', line) # extract FoodOn term ID.
				if len(terms) == 3 and terms[1] in nameless:
					if 'FOODON_' + terms[1] in siren_lookup:
						line = line + '\n\t\t' + '<rdfs:label xml:lang="en">' + siren_lookup['FOODON_' + terms[1]] + '</rdfs:label>'
						#print 'adding label for ',terms[1]
					else:
						print 'couldnt find label in siren_lookup :', terms[1]

			output_handle.write(line)
