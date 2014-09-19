#include "includes.h"
#include "gdeclut.h"
static struct G2DecLutEnt ents[]={
{6,{-1,-1,-1,-1,-1,-1}},
{6,{ 2 , 2 , 2 , 2 , 5 , 5 }},
{6,{ 2 , 2 , 2 , 5 , 2 , 5 }},
{6,{ 2 , 2 , 2 , 5 , 5 , 2 }},
{6,{ 2 , 2 , 2 , 5 , 5 , 5 }},
{6,{ 2 , 2 , 4 , 5 , 5 , 5 }},
{6,{ 2 , 2 , 5 , 2 , 2 , 5 }},
{6,{ 2 , 2 , 5 , 2 , 5 , 2 }},
{6,{ 2 , 2 , 5 , 2 , 5 , 5 }},
{6,{ 2 , 2 , 5 , 4 , 5 , 5 }},
{6,{ 2 , 2 , 5 , 5 , 2 , 2 }},
{6,{ 2 , 2 , 5 , 5 , 2 , 5 }},
{6,{ 2 , 2 , 5 , 5 , 4 , 5 }},
{6,{ 2 , 2 , 5 , 5 , 5 , 2 }},
{6,{ 2 , 2 , 5 , 5 , 5 , 4 }},
{6,{ 2 , 4 , 2 , 5 , 5 , 5 }},
{6,{ 2 , 4 , 5 , 2 , 5 , 5 }},
{6,{ 2 , 4 , 5 , 5 , 2 , 5 }},
{6,{ 2 , 4 , 5 , 5 , 5 , 2 }},
{6,{ 2 , 5 , 2 , 2 , 2 , 5 }},
{6,{ 2 , 5 , 2 , 2 , 5 , 2 }},
{6,{ 2 , 5 , 2 , 2 , 5 , 5 }},
{6,{ 2 , 5 , 2 , 4 , 5 , 5 }},
{6,{ 2 , 5 , 2 , 5 , 2 , 2 }},
{6,{ 2 , 5 , 2 , 5 , 2 , 5 }},
{6,{ 2 , 5 , 2 , 5 , 4 , 5 }},
{6,{ 2 , 5 , 2 , 5 , 5 , 2 }},
{6,{ 2 , 5 , 2 , 5 , 5 , 4 }},
{6,{ 2 , 5 , 4 , 2 , 5 , 5 }},
{6,{ 2 , 5 , 4 , 5 , 2 , 5 }},
{6,{ 2 , 5 , 4 , 5 , 5 , 2 }},
{6,{ 2 , 5 , 5 , 2 , 2 , 2 }},
{6,{ 2 , 5 , 5 , 2 , 2 , 5 }},
{6,{ 2 , 5 , 5 , 2 , 4 , 5 }},
{6,{ 2 , 5 , 5 , 2 , 5 , 2 }},
{6,{ 2 , 5 , 5 , 2 , 5 , 4 }},
{6,{ 2 , 5 , 5 , 4 , 2 , 5 }},
{6,{ 2 , 5 , 5 , 4 , 5 , 2 }},
{6,{ 2 , 5 , 5 , 5 , 2 , 2 }},
{6,{ 2 , 5 , 5 , 5 , 2 , 4 }},
{6,{ 2 , 5 , 5 , 5 , 4 , 2 }},
{6,{ 4 , 2 , 2 , 5 , 5 , 5 }},
{6,{ 4 , 2 , 5 , 2 , 5 , 5 }},
{6,{ 4 , 2 , 5 , 5 , 2 , 5 }},
{6,{ 4 , 2 , 5 , 5 , 5 , 2 }},
{6,{ 4 , 5 , 2 , 2 , 5 , 5 }},
{6,{ 4 , 5 , 2 , 5 , 2 , 5 }},
{6,{ 4 , 5 , 2 , 5 , 5 , 2 }},
{6,{ 4 , 5 , 5 , 2 , 2 , 5 }},
{6,{ 4 , 5 , 5 , 2 , 5 , 2 }},
{6,{ 4 , 5 , 5 , 5 , 2 , 2 }},
{6,{ 5 , 2 , 2 , 2 , 2 , 5 }},
{6,{ 5 , 2 , 2 , 2 , 5 , 2 }},
{6,{ 5 , 2 , 2 , 2 , 5 , 5 }},
{6,{ 5 , 2 , 2 , 4 , 5 , 5 }},
{6,{ 5 , 2 , 2 , 5 , 2 , 2 }},
{6,{ 5 , 2 , 2 , 5 , 2 , 5 }},
{6,{ 5 , 2 , 2 , 5 , 4 , 5 }},
{6,{ 5 , 2 , 2 , 5 , 5 , 2 }},
{6,{ 5 , 2 , 2 , 5 , 5 , 4 }},
{6,{ 5 , 2 , 4 , 2 , 5 , 5 }},
{6,{ 5 , 2 , 4 , 5 , 2 , 5 }},
{6,{ 5 , 2 , 4 , 5 , 5 , 2 }},
{6,{ 5 , 2 , 5 , 2 , 2 , 2 }},
{6,{ 5 , 2 , 5 , 2 , 2 , 5 }},
{6,{ 5 , 2 , 5 , 2 , 4 , 5 }},
{6,{ 5 , 2 , 5 , 2 , 5 , 2 }},
{6,{ 5 , 2 , 5 , 2 , 5 , 4 }},
{6,{ 5 , 2 , 5 , 4 , 2 , 5 }},
{6,{ 5 , 2 , 5 , 4 , 5 , 2 }},
{6,{ 5 , 2 , 5 , 5 , 2 , 2 }},
{6,{ 5 , 2 , 5 , 5 , 2 , 4 }},
{6,{ 5 , 2 , 5 , 5 , 4 , 2 }},
{6,{ 5 , 4 , 2 , 2 , 5 , 5 }},
{6,{ 5 , 4 , 2 , 5 , 2 , 5 }},
{6,{ 5 , 4 , 2 , 5 , 5 , 2 }},
{6,{ 5 , 4 , 5 , 2 , 2 , 5 }},
{6,{ 5 , 4 , 5 , 2 , 5 , 2 }},
{6,{ 5 , 4 , 5 , 5 , 2 , 2 }},
{6,{ 5 , 5 , 2 , 2 , 2 , 2 }},
{6,{ 5 , 5 , 2 , 2 , 2 , 5 }},
{6,{ 5 , 5 , 2 , 2 , 4 , 5 }},
{6,{ 5 , 5 , 2 , 2 , 5 , 2 }},
{6,{ 5 , 5 , 2 , 2 , 5 , 4 }},
{6,{ 5 , 5 , 2 , 4 , 2 , 5 }},
{6,{ 5 , 5 , 2 , 4 , 5 , 2 }},
{6,{ 5 , 5 , 2 , 5 , 2 , 2 }},
{6,{ 5 , 5 , 2 , 5 , 2 , 4 }},
{6,{ 5 , 5 , 2 , 5 , 4 , 2 }},
{6,{ 5 , 5 , 4 , 2 , 2 , 5 }},
{6,{ 5 , 5 , 4 , 2 , 5 , 2 }},
{6,{ 5 , 5 , 4 , 5 , 2 , 2 }},
{6,{ 5 , 5 , 5 , 2 , 2 , 2 }},
{6,{ 5 , 5 , 5 , 2 , 2 , 4 }},
{6,{ 5 , 5 , 5 , 2 , 4 , 2 }},
{6,{ 5 , 5 , 5 , 4 , 2 , 2 }},
{6,{-1,-1,-1,-1,-1,-1}}
};
G2DecLut G2DM24Mk3DecLut={ents,sizeof(ents)/sizeof(struct G2DecLutEnt)};
