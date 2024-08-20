import spacy
import os
import random
import urllib
import filters

nlp = spacy.load("en_core_web_md")
minimum_similarity = 0.85

def get_designer_count():
        #update number of lines in each designer name txt
    designer_filenames = os.listdir("designers")
    designer_count = 0

    #store designer count in a dictionary
    designer_dictionary = {}
    for filename in designer_filenames:
        designer_count = sum(1 for line in open("designers/" + filename))
        designer_dictionary[filename] = designer_count

        #print(designer_count)
    
    return designer_dictionary

designer_count = get_designer_count()

#List of the industries/intended uses of apparel to explore
def find_applications(action):
    if nlp(action).similarity(nlp("applications")) >= minimum_similarity or nlp(action).similarity(nlp("uses")) >= minimum_similarity:
        category = input("""Which category would you like to search in?\n
                            \tWorkwear\n
                            \tOuterwear\n
                            \tSportswear\n
                            \tTactical\n
                            \tLifestyle\n
                            Your search: """)
        
        if nlp(category).similarity(nlp("workwear")) >= minimum_similarity:
            print("""Here are a few workwear apparel brands:\n
                    \tCarhartt - https://www.carhartt.com\n
                    \tDickies - https://www.dickies.com\n
                    \tRed Kap - https://www.redkap.com\n
                    \tTimberland - https://www.timberland.com/timberlandpro\n
                    \tBerne - https://bernedirect.com\n
                    \tDuluth Trading Co. - https://www.duluthtrading.com\n
                    \tHelly Hansen - https://www.hhworkwear.com\n
                    \tWalls - https://www.walls.com/workwear\n
                    \tCaterpillar (CAT) - https://catworkwear.com\n
                    \tWrangler - https://www.wrangler.com/shop/collections-the-work-shop-riggs-workwear\n
                    \tBulwark Protection - https://www.bulwark.com\n
                    \tKEY Apparel - https://www.keyapparel.com\n
                    \tBlaklader (Blåkläder) - https://www.blaklader.com\n
                    \tTough Duck - https://toughduck.com\n
                    \tBen Davis - https://bendavis.com\n
                    \tArborwear - https://arborwear.com\n
                    \tIronclad - https://ironclad.com\n
                    \tKuhl (Kühl) - https://www.kuhl.com\n
                    \tMilwaukee Tool - https://www.milwaukeetool.com/Products/Work-Gear\n
                    \tPatagonia - https://www.patagonia.com/workwear/\n""")
            return

        elif nlp(category).similarity(nlp("outerwear")) >= minimum_similarity:
            print("""Here are a few outerwear/outdoor apparel brands:\n
                    \tThe North Face - https://www.thenorthface.com\n
                    \tPatagonia - https://www.patagonia.com\n
                    \tColumbia Sportswear - https://www.columbia.com\n
                    \tArc\'teryx - https://arcteryx.com\n
                    \tMarmot - https://www.marmot.com\n
                    \tHelly Hansen - https://www.hellyhansen.com\n
                    \tMountain Hardwear - https://www.mountainhardwear.com\n
                    \tCotopaxi - https://www.cotopaxi.com\n
                    \tFjallraven (Fjällräven) - https://www.fjallraven.com\n
                    \tRab - https://rab.equipment\n
                    \tEddie Bauer - https://www.eddiebauer.com\n
                    \tCanada Goose - https://www.canadagoose.com\n
                    \tBlack Diamond - https://www.blackdiamondequipment.com\n
                    \tACRONYM® - https://acrnm.com\n
                    \tOutdoor Research - https://www.outdoorresearch.com\n
                    \tFilson - http://filson.com\n
                    \tBerghaus - https://www.berghaus.com\n
                    \tJack Wolfskin - https://www.jack-wolfskin.com\n
                    \tREI Co-op - https://www.rei.com\n
                    \tVAUDE - https://www.vaude.com\n
                    \tprAna - https://www.prana.com\n
                    \tHaglofs (Haglöfs) - https://www.haglofs.com\n""")
            return

        elif nlp(category).similarity(nlp("sportswear")) >= minimum_similarity:
            print("""Here are a few sportswear apparel brands:\n
                    \tNike - https://www.nike.com\n
                    \tAdidas - https://www.adidas.com\n
                    \tPuma - https://puma.com\n
                    \tUnder Armour - https://www.underarmour.com/\n
                    \tReebok - https://www.reebok.com\n
                    \tASICS - https://www.asics.com\n
                    \tNew Balance - https://www.newbalance.com\n
                    \tLululemon - https://shop.lululemon.com\n
                    \tColumbia Sportswear - https://columbia.com\n
                    \tMizuno - https://mizuno.com\n
                    \tEllesse - https://ellesse.us\n
                    \tOakley -  https://www.oakley.com/en-us\n
                    \tBlack Diamond - https://www.blackdiamondequipment.com\n
                    \tDiadora - https://www.diadora.com\n
                    \tSpeedo - https://www.speedo.com\n
                    \tQuiksilver - https://www.quiksilver.com\n
                    \tSalomon - https://www.salomon.com\n
                    \tBrooks - https://www.brooksrunning.com\n
                    \tHoka One One - https://www.hoka.com\n
                    \tUmbro - https://www.umbro.com\n
                    \tSaucony - https://www.saucony.com\n
                    \tThe North Face - https://www.thenorthface.com\n
                    \tPatagonia - https://www.patagonia.com\n
                    \tArc\'teryx - https://arcteryx.com\n
                    \tOutdoor Research - https://www.outdoorresearch.com\n
                    \tRab - https://rab.equipment\n
                    \tLa Sportiva - https://www.lasportivausa.com\n
                    \tMammut - https://www.mammut.com\n
                    \tPetzl - https://www.petzl.com\n
                    \tEdelrid - https://edelrid.com\n
                    \tGrivel - https://grivel.com/\n
                    \tMontane - https://montane.com\n
                    \tSo iLL - https://soillholds.com\n
                    \tMetolius - https://www.metoliusclimbing.com\n
                    \tAlpinestars - https://www.alpinestars.com\n
                    \tSparco - https://www.sparcousa.com\n
                    \tOMP Racing - https://www.us.ompracing.com\n
                    \tBell Racing - https://bellracing.com\n
                    \tArai Helmets - https://www.araiamericas.com/helmets\n
                    \tStilo - https://www.stilohelmets.com\n
                    \tFox Racing - https://www.foxracing.com\n
                    \tRST - https://www.rst-moto.com\n
                    \tRev'it! - https://www.revitsport.com\n
                    \tOGIO - https://ogiopowersports.com\n
                    \tFairtex - https://www.fairtex.com\n
                    \tYOKKAO - https://yokkao.com\n
                    \tEverlast - https://www.everlast.com\n
                    \tTusah - https://www.tusah.com\n
                    \tMooto - https://www.mooto.com\n
                    \tBad Boy - http://badboy.com\n
                    \tVenum - https://www.venum.com\n""")
            return

        elif nlp(category).similarity(nlp("tactical")) >= minimum_similarity:
            print("""Here are a few brands producing tactical gear:\n
                    	\t5.11 Tactical - https://www.511tactical.com/\n
	                    \tPropper - https://www.propper.com/\n
                        \tCondor Outdoor - https://www.condoroutdoor.com/\n
                        \tBlackhawk - https://www.blackhawk.com/\n
                        \tTRU-SPEC - https://www.truspec.com/\n
                        \tVertx - https://vertx.com/\n
                        \tUnder Armour Tactical - https://www.underarmour.com/en-us/tactical\n
                        \tFirst Tactical - https://www.firsttactical.com/\n
                        \tCrye Precision - https://www.cryeprecision.com/\n
                        \tArc\'teryx LEAF - https://leaf.arcteryx.com/\n
                        \tPatagonia TAA - https://www.patagonia.com/tactical/\n
                        \tHelikon-Tex - https://www.helikon-tex.com/\n
                        \tUF PRO - https://ufpro.com/\n
                        \tKitanica - https://kitanica.com/\n
                        \tSKD Tactical - https://www.skdtac.com/\n
                        \tViktos - https://www.viktos.com/\n
                        \tLA Police Gear (LAPG) - https://www.lapolicegear.com/\n
                        \tTactical Distributors - https://tacticaldistributors.com/\n
                        \tMassif - https://www.massif.com/\n
                        \tOakley SI - https://www.oakleysi.com/\n
                        \tRothco - https://www.rothco.com/\n
                        \tBeyond Clothing - https://beyondclothing.com/\n
                        \tGrey Ghost Gear - https://greyghostgear.com/\n
                        \tEberlestock - https://eberlestock.com/\n
                        \tBlauer Tactical - https://www.blauer.com/\n""")
            
            return
            
        elif nlp(category).similarity(nlp("lifestyle")) >= minimum_similarity:
            print("""Here are a few popular lifestyle brands:\n
                        \tPatagonia - https://www.patagonia.com/\n
                        \tLevi's - https://www.levi.com/\n
                        \tNike - https://www.nike.com/\n
                        \tAdidas - https://www.adidas.com/\n
                        \tRalph Lauren - https://www.ralphlauren.com/\n
                        \tCarhartt - https://www.carhartt.com/\n
                        \tTommy Hilfiger - https://usa.tommy.com/\n
                        \tLululemon - https://shop.lululemon.com/\n
                        \tCalvin Klein - https://www.calvinklein.us/\n
                        \tAllSaints - https://www.allsaints.com/\n
                        \tJack & Jones - https://www.jackjones.com/\n
                        \tVans - https://www.vans.com/\n
                        \tGap - https://www.gap.com/\n
                        \tVolcom - https://www.volcom.com/\n
                        \tChampion - https://www.champion.com/\n
                        \tPolo Ralph Lauren - https://www.ralphlauren.com/polo-ralph-lauren\n
                        \tJ.Crew - https://www.jcrew.com/\n
                        \tH&M - https://www.hm.com/\n
                        \tZara - https://www.zara.com/\n
                        \tUrban Outfitters - https://www.urbanoutfitters.com/\n
                        \tUNIQLO - https://www.uniqlo.com/\n
                        \tAbercrombie & Fitch - https://www.abercrombie.com/\n
                        \tFree People - https://www.freepeople.com/\n
                        \tMadewell - https://www.madewell.com/\n
                        \tReebok - https://www.reebok.com/\n
                        \tFjällräven - https://www.fjallraven.com/\n
                        \tPuma - https://us.puma.com/\n
                        \tColumbia - https://www.columbia.com/\n
                        \tNew Balance - https://www.newbalance.com/\n
                        \tG-Star RAW - https://www.g-star.com/\n
                        \tBrooks Brothers - https://www.brooksbrothers.com/\n
                        \tLacoste - https://www.lacoste.com/\n
                        \tFilson - https://www.filson.com/\n
                        \tAmerican Eagle - https://www.ae.com/\n
                        \tRVCA - https://www.rvca.com/\n
                        \tThe North Face - https://www.thenorthface.com/\n
                        \tBanana Republic - https://bananarepublic.gap.com/\n
                        \tTimberland - https://www.timberland.com/\n
                        \tHerschel Supply Co. - https://herschel.com/\n
                        \tOuterknown - https://www.outerknown.com/""")
            return
        
        else:
            print("""Sorry, I don't understand that input. Try \"workwear\", \"outerwear\",
                        \"sportswear\", \"tactical\", or \"lifestyle\".\n""")
        
        return
    
    return

#Show me something random or interesting
def discover(action):
    input = action
    if nlp(action).similarity(nlp("random")) >= minimum_similarity or nlp(action).similarity(nlp("interesting")) >= minimum_similarity:
        discovery_category = input("Would you like a designer in menswear, womenswear, or everything else?: ")
        category_file = "none"

        if nlp(discovery_category).similarity(nlp("menswear")) >= minimum_similarity or nlp(action).similarity(nlp("mens")) >= minimum_similarity:
            category_file = "menswear_designers.txt"

        elif nlp(discovery_category).similarity(nlp("womenswear")) >= minimum_similarity or nlp(action).similarity(nlp("womens")) >= minimum_similarity:
            category_file = "womenswear_designers.txt"

        elif nlp(discovery_category).similarity(nlp("everything else")) >= minimum_similarity or nlp(action).similarity(nlp("other")) >= minimum_similarity:
            category_file = "misc_items_designers.txt"
        
        else:
            return
        
        random_designer = random.randint(1, designer_count[category_file])

        with open("designers/" + category_file) as file:
            content = file.readlines()

            #print designer's name from file, subtract 1 from random_designer to get index
            print("Here's designer " + content[random_designer - 1])

        # exit out
    elif nlp(action).similarity(nlp("exit")) >= minimum_similarity or nlp(action).similarity(nlp("escape")) >= minimum_similarity:
        return
        
    elif nlp(action).similarity(nlp("brands")) >= minimum_similarity or nlp(action).similarity(nlp("designers")) >= minimum_similarity:
        filters.find_brand(action)
        return
    return

#Show me advice or inspiration
def advice_or_insipration(action):
    if nlp(action).similarity(nlp("advice")) >= minimum_similarity or nlp(action).similarity(nlp("tips")) >= minimum_similarity:
        print("""Here are a couple resources for tips and advice:\n
                https://www.youtube.com/@FrugalAesthetic\n
                https://www.youtube.com/@DrewJoiner\n""")
            
    elif nlp(action).similarity(nlp("inspiration")) >= minimum_similarity or nlp(action).similarity(nlp("ideas")) >= minimum_similarity:
        print("""Here are a few resources for ideas and inspiration:
                https://www.youtube.com/@imdanielsimmons\n
                https://www.youtube.com/@Yesiluvmarii\n
                https://www.instagram.com/wisdm/\n
                https://www.instagram.com/hartcopy/\n""")
        
    else:
        return    
        
    return

# Piece or name (top, bottom, shoe, etc.)
def specific_search(action):
    if nlp(action).similarity(nlp("specific")) >= minimum_similarity or nlp(action).similarity(nlp("something specific")) >= minimum_similarity:
        search = input("Your search: ")
        print("""Here are a few results for \"{0}\":
                \thttps://stockx.com/search?s={1}\n
                \thttps://www.ssense.com/en-us/men?q={1}\n
                \thttps://www.ssense.com/en-us/women?q={1}\n
                \thttps://www.goat.com/search?query={1}\n
                \thttps://www.asos.com/us/search/?q={1}\n
                Alternatively, buy in-person (e.g thrifting) or search on:\n
                \t\"grailed {0}\"\n
                \t\"{0}\"""".format(search, urllib.parse.quote_plus(search)))
    return

