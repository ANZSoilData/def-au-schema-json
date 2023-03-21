# ANSIS Soil Domain Enumerations
**JSON Schema Location:** https://anzsoildata.github.io/def-au-schema-json/schema/domain/2023-06-30/enum.json

ANSIS controlled vocabularies converted to JSON schema enumerations. Follow the link under the vocabulary's title for full definitions.

> Enumerations defined according to the pattern recommended here: https://github.com/json-schema-org/json-schema-spec/issues/57

## ANSIS Entity Types

**ANSIS Vocabulary Location:** https://anzsoil.org/def/au/domain

Core ANSIS entities (features) served by the ANSIS system.

| JSON Value | Preferred Label | Definition Link |
| ---------- | --------------- | --------------- |
| ansis:LandSurveySite | Land Survey Site | |
| ansis:SoilBody | Soil Body | |
| ansis:SoilHorizon | Soil Horizon | |
| ansis:SoilLayer | Soil Layer | |
| ansis:SoilProfile | Soil Profile | |
| ansis:Soilample | Soil Sample | |
| ansis:SoilSite | Soil Site | |
| ansis:SoilSurface | Soil Surface | |
| ansis:Substrate | Substrate | |
| ansis:Treatment | Treatment | |
## Stream channel development - enumeration

**ANSIS Vocabulary Location:** [lf:Channel-development](http://anzsoil.org/def/au/asls/landform/Channel-development)

The degree of development of stream channels.

| JSON Value | Preferred Label | Definition Link |
| ---------- | --------------- | --------------- |
| lf:stream-channel-development-A | Alluvial | |
| lf:stream-channel-development-E | Erosional | |
| lf:stream-channel-development-I | Incipient | |
| lf:stream-channel-development-O | Absent | |
## Stream-wise channel pattern - enumeration

**ANSIS Vocabulary Location:** [lf:Channel-pattern](http://anzsoil.org/def/au/asls/landform/Channel-pattern)

In a traverse downstream, it may happen that tributaries enter the stream at frequent intervals, or that the stream splits into distributaries, or that these tendencies are absent (the non-tributary case) or are in balance with each other (the braided or anastomotic case called here reticulated) giving four classes of stream-wise channel pattern.

| JSON Value | Preferred Label | Definition Link |
| ---------- | --------------- | --------------- |
| lf:streamwise-channel-pattern-D | Distributary | |
| lf:streamwise-channel-pattern-N | Non-tributary | |
| lf:streamwise-channel-pattern-R | Reticulated | |
| lf:streamwise-channel-pattern-T | Tributary | |
## Abundance of coarse fragments - enumeration

**ANSIS Vocabulary Location:** [ls:Coarse-fragments-abundance](http://anzsoil.org/def/au/asls/land-surface/Coarse-fragments-abundance)

The percentage of coarse fragments.

| JSON Value | Preferred Label | Definition Link |
| ---------- | --------------- | --------------- |
| ls:coarse-fragments-abundance-0 | No coarse fragments | |
| ls:coarse-fragments-abundance-1 | Very slightly or very few | |
| ls:coarse-fragments-abundance-2 | Slightly or few | |
| ls:coarse-fragments-abundance-3 | No qualifier or common | |
| ls:coarse-fragments-abundance-4 | Moderately or many | |
| ls:coarse-fragments-abundance-5 | Very or abundant | |
| ls:coarse-fragments-abundance-6 | Extremely or very abundant | |
## Shape of coarse fragments - enumeration

**ANSIS Vocabulary Location:** [ls:Coarse-fragments-shape](http://anzsoil.org/def/au/asls/land-surface/Coarse-fragments-shape)

The shape of coarse fragments is determined by referencing the chart that captures the roundness and sphericity. (Figure 12)

| JSON Value | Preferred Label | Definition Link |
| ---------- | --------------- | --------------- |
| ls:coarse-fragments-shape-A | Angular | |
| ls:coarse-fragments-shape-AP | Angular platy | |
| ls:coarse-fragments-shape-AT | Angular tabular | |
| ls:coarse-fragments-shape-R | Rounded | |
| ls:coarse-fragments-shape-RP | Rounded platy | |
| ls:coarse-fragments-shape-RT | Rounded tabular | |
| ls:coarse-fragments-shape-S | Subangular | |
| ls:coarse-fragments-shape-SP | Subangular platy | |
| ls:coarse-fragments-shape-ST | Subangular tabular | |
| ls:coarse-fragments-shape-U | Subrounded | |
| ls:coarse-fragments-shape-UP | Subrounded platy | |
| ls:coarse-fragments-shape-UT | Subrounded tabular | |
## Moisture status for colour description - enumeration

**ANSIS Vocabulary Location:** [sp:Colour-moisture-status](http://anzsoil.org/def/au/asls/soil-profile/Colour-moisture-status)

Moisture status for colour description

| JSON Value | Preferred Label | Definition Link |
| ---------- | --------------- | --------------- |
| sp:colour-stat-D | Dry (colour status) | |
| sp:colour-stat-M | Moist | |
## Abundance of cutans - enumeration

**ANSIS Vocabulary Location:** [sp:Cutans-abundance](http://anzsoil.org/def/au/asls/soil-profile/Cutans-abundance)

Abundance of cutans

| JSON Value | Preferred Label | Definition Link |
| ---------- | --------------- | --------------- |
| sp:cutans-abundance-0 | No cutans | |
| sp:cutans-abundance-1 | Few (cutans abundance) | |
| sp:cutans-abundance-2 | Common (cutans abundance) | |
| sp:cutans-abundance-3 | Many (cutans abundance) | |
## Disturbance of site - enumeration

**ANSIS Vocabulary Location:** [ls:Disturbance-of-site](http://anzsoil.org/def/au/asls/land-surface/Disturbance-of-site)

These are broad categories of disturbance. Users may subdivide where considered necessary.

| JSON Value | Preferred Label | Definition Link |
| ---------- | --------------- | --------------- |
| ls:disturbance-of-site-0 | No effective disturbance; natural | |
| ls:disturbance-of-site-1 | No effective disturbance other than grazing by hoofed animals | |
| ls:disturbance-of-site-2 | Limited clearing | |
| ls:disturbance-of-site-3 | Extensive clearing | |
| ls:disturbance-of-site-4 | Complete clearing; pasture, native or improved, but never cultivated | |
| ls:disturbance-of-site-5 | Complete clearing; pasture, native or improved, cultivated at some stage | |
| ls:disturbance-of-site-6 | Cultivation; rainfed | |
| ls:disturbance-of-site-7 | Cultivation; irrigated, past or present | |
| ls:disturbance-of-site-8 | Highly disturbed | |
## Mineral soils field texture grade - enumeration

**ANSIS Vocabulary Location:** [sp:Field-texture-mineral](http://anzsoil.org/def/au/asls/soil-profile/Field-texture-mineral)

The following description of determination of field texture is adapted from Northcote (1979).
Field texture is a measure of the behaviour of a small handful of soil when moistened and kneaded into a ball and then pressed out between thumb and forefinger.
Take a sample of soil sufficient to fit comfortably into the palm of the hand. Moisten the soil with water, a little at a time, and knead until the ball of soil, so formed, just fails to stick to the fingers. Add more soil or water to attain this condition, known as the sticky point, which approximates field capacity for that soil. Continue kneading and moistening until there is no apparent change in the soil ball, usually a working time of 1–2 minutes. The soil ball, or bolus, is now ready for shearing manipulation, but the behaviour of the soil during bolus formation is also indicative of its field texture. The behaviour of the bolus and of the ribbon produced by shearing (pressing out) between thumb and forefinger characterises the field texture. Do not assess field texture grade solely on the length of ribbon.
The recommended field texture grades as characterised by the behaviour of the moist bolus are described. The approximate percentage content of clay (particles less than 0.002 mm in diameter) and silt (particles between 0.02 and 0.002 mm in diameter) are given as a guide. These percentages must not be used to determine a field texture, that is, do not use them to convert a laboratory particle size value to a field texture grade. Similarly, do not adjust a field texture grade when laboratory particle size data become available.

| JSON Value | Preferred Label | Definition Link |
| ---------- | --------------- | --------------- |
| sp:field-texture-CL | Clay loam | |
| sp:field-texture-CLS | Clay loam, sandy | |
| sp:field-texture-CS | Clayey sand | |
| sp:field-texture-HC | Heavy clay | |
| sp:field-texture-L | Loam | |
| sp:field-texture-LC | Light clay | |
| sp:field-texture-LMC | Light medium clay | |
| sp:field-texture-LS | Loamy sand | |
| sp:field-texture-MC | Medium clay | |
| sp:field-texture-MHC | Medium heavy clay | |
| sp:field-texture-S | Sand (field texture) | |
| sp:field-texture-SCL | Sandy clay loam | |
| sp:field-texture-SL | Sandy loam | |
| sp:field-texture-ZCL | Silty clay loam | |
| sp:field-texture-ZL | Silty loam | |
## Organic soils field texture - enumeration

**ANSIS Vocabulary Location:** [sp:Field-texture-organic](http://anzsoil.org/def/au/asls/soil-profile/Field-texture-organic)

Organic soils do not have textural grades, as soil texture is determined by the size of mineral particles finer than 2 mm (NCST). In a sense, organic soils do have a texture related to the plant materials from which they formed and the degree of decomposition, exposure and drying. These field texture names may be used to characterise materials that on field examination are considered to be clearly dominated by organic matter. Peats may be assessed by examining the degree of decomposition and distinctness of plant remains. This work is adapted from Soil Survey Staff (1975) and Avery (1980).

| JSON Value | Preferred Label | Definition Link |
| ---------- | --------------- | --------------- |
| sp:field-texture-AP | Sapric peat | |
| sp:field-texture-CP | Clayey peat | |
| sp:field-texture-GP | Granular peat | |
| sp:field-texture-HP | Hemic peat | |
| sp:field-texture-IP | Fibric peat | |
| sp:field-texture-LP | Loamy peat | |
| sp:field-texture-SP | Sandy peat | |
## Horizon suffixes

**ANSIS Vocabulary Location:** [sp:Horizon-suffix](http://anzsoil.org/def/au/asls/soil-profile/Horizon-suffix)

The horizon's alphabetic suffix is used to further define the horizon. It always comes after the numeric subdivision except for suffix p, where the number always follows the letter (e.g. Ap2).

| JSON Value | Preferred Label | Definition Link |
| ---------- | --------------- | --------------- |
| sp:horizon-suffix-b | Horizon suffix b | |
| sp:horizon-suffix-c | Horizon suffix c | |
| sp:horizon-suffix-d | Horizon suffix d | |
| sp:horizon-suffix-e | Horizon suffix e | |
| sp:horizon-suffix-f | Horizon suffix f | |
| sp:horizon-suffix-g | Horizon suffix g | |
| sp:horizon-suffix-h | Horizon suffix h | |
| sp:horizon-suffix-j | Horizon suffix j | |
| sp:horizon-suffix-k | Horizon suffix k | |
| sp:horizon-suffix-m | Horizon suffix m | |
| sp:horizon-suffix-p | Horizon suffix p | |
| sp:horizon-suffix-q | Horizon suffix q | |
| sp:horizon-suffix-r | Horizon suffix r | |
| sp:horizon-suffix-s | Horizon suffix s | |
| sp:horizon-suffix-t | Horizon suffix t | |
| sp:horizon-suffix-w | Horizon suffix w | |
| sp:horizon-suffix-x | Horizon suffix x | |
| sp:horizon-suffix-y | Horizon suffix y | |
| sp:horizon-suffix-z | Horizon suffix z | |
## Duration (annual) of inundation - enumeration

**ANSIS Vocabulary Location:** [ls:Inundation-duration](http://anzsoil.org/def/au/asls/land-surface/Inundation-duration)

Give likely duration of an inundation event.

| JSON Value | Preferred Label | Definition Link |
| ---------- | --------------- | --------------- |
| ls:inundation-duration-1 | Less than 1 day | |
| ls:inundation-duration-2 | Between 1 and 20 days | |
| ls:inundation-duration-3 | Between 20 and 120 days | |
| ls:inundation-duration-4 | More than 120 days | |
## Morphological type - enumeration

**ANSIS Vocabulary Location:** [lf:Landform-element-type](http://anzsoil.org/def/au/asls/landform/Landform-element-type)

Landform elements fall into morphological types as sketched in Figure 1. Ten types are distinguished.

| JSON Value | Preferred Label | Definition Link |
| ---------- | --------------- | --------------- |
| lf:Relative-inclination | Relative inclination of slope elements - enumeration | |
| lf:compound-morphological-types | Compound morphological types - enumeration | |
| lf:morphological-type-C | Crest | |
| lf:morphological-type-D | Closed depression | |
| lf:morphological-type-F | Flat | |
| lf:morphological-type-H | Hillock | |
| lf:morphological-type-L | Lower slope (requires inclination modifier) | |
| lf:morphological-type-LA | Lower slope Maximal | |
| lf:morphological-type-LI | Lower slope Minimal | |
| lf:morphological-type-LN | Lower slope Waning | |
| lf:morphological-type-LX | Lower slope Waxing | |
| lf:morphological-type-M | Mid-slope (requires inclination modifier) | |
| lf:morphological-type-MA | Mid-slope Maximal | |
| lf:morphological-type-MI | Mid-slope Minimal | |
| lf:morphological-type-MN | Mid-slope Waning | |
| lf:morphological-type-MX | Mid-slope Waxing | |
| lf:morphological-type-R | Ridge | |
| lf:morphological-type-S | Simple slope | |
| lf:morphological-type-U | Upper slope (requires inclination modifier) | |
| lf:morphological-type-UA | Upper slope Maximal | |
| lf:morphological-type-UI | Upper slope Minimal | |
| lf:morphological-type-UN | Upper slope Waning | |
| lf:morphological-type-UX | Upper slope Waxing | |
| lf:morphological-type-V | Open depression (vale) | |
## Lithology of coarse fragments - enumeration

**ANSIS Vocabulary Location:** [ls:Lithology-coarse-fragments](http://anzsoil.org/def/au/asls/land-surface/Lithology-coarse-fragments)

The lithology of the coarse fragments is usually identified as coming from the substrate or from rock outcrop. Where the lithology of the coarse fragments is different from that of the substrate material and/or rock outcrop, describe it as for lithology of substrate material only where the rock type is definitely known or is confidently presumed. Some coarse fragments are commonly encountered that are not directly related to the substrate material.    

| JSON Value | Preferred Label | Definition Link |
| ---------- | --------------- | --------------- |
| ls:lithology-CC | Charcoal | |
| ls:lithology-IS | Ironstone | |
| ls:lithology-M | Same as substrate material | |
| ls:lithology-OT | Other | |
| ls:lithology-OW | Opalised wood | |
| ls:lithology-PU | Pumice | |
| ls:lithology-R | Same as rock outcrop | |
| ls:lithology-SS | Shells | |
## Biotic microrelief agents - enumeration

**ANSIS Vocabulary Location:** [ls:Microrelief-agent-biotic](http://anzsoil.org/def/au/asls/land-surface/Microrelief-agent-biotic)

The biotic agents causing the relief.

| JSON Value | Preferred Label | Definition Link |
| ---------- | --------------- | --------------- |
| ls:biotic-microrelief-agent-A | Ant | |
| ls:biotic-microrelief-agent-B | Bird | |
| ls:biotic-microrelief-agent-M | Human | |
| ls:biotic-microrelief-agent-N | Animal | |
| ls:biotic-microrelief-agent-O | Other | |
| ls:biotic-microrelief-agent-T | Termite | |
| ls:biotic-microrelief-agent-V | Vegetation | |
## Mottle abundance - enumeration

**ANSIS Vocabulary Location:** [sp:Mottle-abundance](http://anzsoil.org/def/au/asls/soil-profile/Mottle-abundance)

The percentage of mottles is estimated by eye using the chart in Figure 11 (ASLSFH3Ed) for comparison. 

| JSON Value | Preferred Label | Definition Link |
| ---------- | --------------- | --------------- |
| sp:mottle-abundance-0 | No mottles or other colour patterns | |
| sp:mottle-abundance-1 | Very few (mottle abundance) | |
| sp:mottle-abundance-2 | Few (mottle abundance) | |
| sp:mottle-abundance-3 | Common (mottle abundance) | |
| sp:mottle-abundance-4 | Many (mottle abundance) | |
## Cementation of pan - enumeration

**ANSIS Vocabulary Location:** [sp:Pans-cementation](http://anzsoil.org/def/au/asls/soil-profile/Pans-cementation)

Place a 30 mm diameter piece of the pan in water for 1 hour. If it slakes, it is uncemented; if not, it is cemented. The degree of cementation is assessed on the following scale after the 1 hour soaking in water.

| JSON Value | Preferred Label | Definition Link |
| ---------- | --------------- | --------------- |
| sp:pans-cementation-0 | Uncemented | |
| sp:pans-cementation-1 | Weakly cemented | |
| sp:pans-cementation-2 | Moderately cemented | |
| sp:pans-cementation-3 | Strongly cemented | |
| sp:pans-cementation-4 | Very strongly cemented | |
## Pedal soil grades - enumeration

Pedal soils have observable peds and are divided into: sp:structure-pedality-grade-M, sp:structure-pedality-grade-S and sp:structure-pedality-grade-W. Apedal soils have no observable peds and are divided into: sp:structure-pedality-grade-G and sp:structure-pedality-grade-V

| JSON Value | Preferred Label | Definition Link |
| ---------- | --------------- | --------------- |
| sp:structure-pedality-grade-M | Moderate (structure pedality grade) | |
| sp:structure-pedality-grade-S | Strong (structure pedality grade) | |
| sp:structure-pedality-grade-W | Weak (structure pedality grade) | |
| sp:structure-pedality-grade-G | Single grain | |
| sp:structure-pedality-grade-V | Massive (structure pedality grade) | |
## Size of peds

**ANSIS Vocabulary Location:** [sp:Pedality-size](http://anzsoil.org/def/au/asls/soil-profile/Pedality-size)

The average least dimension of peds is used to determine the class interval. Use figure 17. The least dimension is the vertical dimension for platy structure; the horizontal dimension for prismatic, columnar, blocky and polyhedral peds; the maximum separation of convex faces for lenticular peds; and the diameter for granular peds.

| JSON Value | Preferred Label | Definition Link |
| ---------- | --------------- | --------------- |
| sp:structure-pedality-size-1 | < 2 mm | |
| sp:structure-pedality-size-2 | 2-5 mm | |
| sp:structure-pedality-size-3 | 5-10 mm | |
| sp:structure-pedality-size-4 | 10-20 mm | |
| sp:structure-pedality-size-5 | 20-50 mm | |
| sp:structure-pedality-size-6 | 50-100 mm | |
| sp:structure-pedality-size-7 | 100-200 mm | |
| sp:structure-pedality-size-8 | 200-500 mm | |
| sp:structure-pedality-size-9 | > 500 mm | |
## Abundance of very fine, fine, medium and coarse macropores

Abundance of very fine and fine macropores (less than 2mm diameter), and medium and coarse macropores (greater than 2 mm diameter).

| JSON Value | Preferred Label | Definition Link |
| ---------- | --------------- | --------------- |
| sp:voids-macropores-abundance-0 | No macropores | |
| sp:voids-macropores-abundance-1 | Few fine or very fine macropores | |
| sp:voids-macropores-abundance-2 | Common fine or very fine macropores | |
| sp:voids-macropores-abundance-3 | Many fine or very fine macropores | |
| sp:voids-macropores-abundance-4 | Few medium or coarse macropores | |
| sp:voids-macropores-abundance-5 | Common medium or coarse macropores | |
| sp:voids-macropores-abundance-6 | Many medium or coarse macropores | |
## Abundance of rock outcrop - enumeration

**ANSIS Vocabulary Location:** [ls:Rock-outcrop-abundance](http://anzsoil.org/def/au/asls/land-surface/Rock-outcrop-abundance)

Abundance of rock outcrop.

| JSON Value | Preferred Label | Definition Link |
| ---------- | --------------- | --------------- |
| ls:rock-outcrop-abundance-0 | No rock outcrop | |
| ls:rock-outcrop-abundance-1 | Very slightly rocky | |
| ls:rock-outcrop-abundance-2 | Slightly rocky | |
| ls:rock-outcrop-abundance-3 | Rocky | |
| ls:rock-outcrop-abundance-4 | Very rocky | |
| ls:rock-outcrop-abundance-5 | Rockland | |
## Root abundance - enumeration

**ANSIS Vocabulary Location:** [sp:Root-abundance](http://anzsoil.org/def/au/asls/soil-profile/Root-abundance)

Number of roots per 0.01 m2 (100 mm × 100 mm)

| JSON Value | Preferred Label | Definition Link |
| ---------- | --------------- | --------------- |
| sp:roots-abundance-0 | No roots | |
| sp:roots-abundance-1 | Few (roots abundance) | |
| sp:roots-abundance-2 | Common (roots abundance) | |
| sp:roots-abundance-3 | Many (roots abundance) | |
| sp:roots-abundance-4 | Abundant (roots abundance) | |
## Abundance of segregations - enumeration

**ANSIS Vocabulary Location:** [sp:Segregations-abundance](http://anzsoil.org/def/au/asls/soil-profile/Segregations-abundance)

Abundance of segregations. Use figure 11 as a guide.

| JSON Value | Preferred Label | Definition Link |
| ---------- | --------------- | --------------- |
| sp:segregations-abundance-0 | No segregations | |
| sp:segregations-abundance-1 | Very few (segregations abundance) | |
| sp:segregations-abundance-2 | Few (segregations abundance) | |
| sp:segregations-abundance-3 | Common (segregations abundance) | |
| sp:segregations-abundance-4 | Many (segregations abundance) | |
| sp:segregations-abundance-5 | Very many (segregations abundance) | |
## Permeability - enumeration

**ANSIS Vocabulary Location:** [sp:Soil-permeability](http://anzsoil.org/def/au/asls/soil-profile/Soil-permeability)

Permeability is independent of climate and drainage, and – as applied to a soil – is controlled by the potential to transmit water (saturated hydraulic conductivity, Ks) of the least permeable layer in the soil. Therefore it is inferred from attributes of the soil such as structure, texture, porosity, cracks and shrink–swell properties. The rate of transmission of water in the profile is based on the assumption that loss by evapotranspiration is minimal. The Ks ranges are compatible with those of Nowland in Canada, as reported by McKeague et al. (1982).

| JSON Value | Preferred Label | Definition Link |
| ---------- | --------------- | --------------- |
| sp:soil-water-permeability-1 | Very slowly permeable | |
| sp:soil-water-permeability-2 | Slowly permeable | |
| sp:soil-water-permeability-3 | Moderately permeable | |
| sp:soil-water-permeability-4 | Highly permeable | |
## Soil Water Drainage

**ANSIS Vocabulary Location:** [sp:Site-drainage](http://anzsoil.org/def/au/asls/soil-profile/Site-drainage)

Drainage is a useful term to summarise local soil wetness conditions, that is, it provides a statement about soil and site drainage likely to occur in most years. It is affected by a number of attributes, both internal and external, that may act separately or together. Internal attributes include soil structure, texture, porosity, hydraulic conductivity, and water-holding capacity, while external attributes are source and quality of water, evapotranspiration, gradient and length of slope, and position in the landscape.

| JSON Value | Preferred Label | Definition Link |
| ---------- | --------------- | --------------- |
| sp:soil-water-drainage-1 | very poorly drained | |
| sp:soil-water-drainage-2 | poorly drained | |
| sp:soil-water-drainage-3 | imperfectly drained | |
| sp:soil-water-drainage-4 | moderately well drained | |
| sp:soil-water-drainage-5 | well drained | |
| sp:soil-water-drainage-6 | rapidly drained | |
## Condition of surface soil when dry - enumeration

**ANSIS Vocabulary Location:** [sp:Surface-condition](http://anzsoil.org/def/au/asls/soil-profile/Surface-condition)

Many surface soils have a characteristic appearance when dry. Because surface conditions are often relevant to the use of the soil and indicative of particular kinds of soil, every effort should be made to observe the surface condition in the dry state. The surface conditions are not necessarily mutually exclusive:

| JSON Value | Preferred Label | Definition Link |
| ---------- | --------------- | --------------- |
| sp:surfacecondition-C | Surface crust | |
| sp:surfacecondition-F | Firm (surface condition) | |
| sp:surfacecondition-G | Cracking | |
| sp:surfacecondition-H | Hard setting | |
| sp:surfacecondition-L | Loose (surface condition) | |
| sp:surfacecondition-M | Self-mulching | |
| sp:surfacecondition-O | Other (surface condition) | |
| sp:surfacecondition-P | Poached | |
| sp:surfacecondition-R | Recently cultivated | |
| sp:surfacecondition-S | Soft | |
| sp:surfacecondition-T | Trampled | |
| sp:surfacecondition-X | Surface flake | |
| sp:surfacecondition-Y | Cryptogam surface | |
| sp:surfacecondition-Z | Saline (surface condition) | |
## To Be Defined

Placeholder for enumerations yet to be created.

| JSON Value | Preferred Label | Definition Link |
| ---------- | --------------- | --------------- |
| xx:a | value a | |
| xx:b | value b | |