grammar Flu;     

program: sentence;

sentence: require | ask | checkStats | symptom;

require: verb (phrase)? (ON|IN)? (date)?;
ask: WHAT (IS)? TM? (cycleStatus | specificPharse) QUESTIONMARK;
checkStats: CHECK CYCLE STATS;
symptom: dateInWord I FEEL symp;

verb: START | END | SHOW;
symp : (SYMP COMMA symp) | SYMP ;
phrase: (OVU | PER | FER | NONF)  CYCLE;

cycleStatus: CYCLE STATUS (ON|IN)? date;
specificPharse : (OVU | PER | FER | NONF) (DAYS)? (ON|IN)? dateMonth;


date: (dateCompare| dateInNum| dateInWord);
dateInNum: NUMBER SLASH NUMBER SLASH NUMBER;
dateInWord: 'tomorrow'|'today'|'yesterday';
dateCompare: NUMBER DAYS BeforeAfter;
dateMonth: monthWord| monthCompare;

monthWord: WHEN MO;
monthCompare: NUMBER MO BeforeAfter;

TM: THE|MY;
BeforeAfter: BEFORE|AFTER;


WHAT: 'what'|'What';
IS: 'is';
THE: 'the';
MY: 'my';
STATUS: 'status';
CHECK:'check'| 'Check';
STATS: 'statistic';
START: 'start'| 'Start';
END: 'End'| 'end';
SHOW: 'show'| 'Show';
ON: 'on';
IN: 'in';
WHEN: 'this'|'previous'|'next';
I :'i';
FEEL : 'feel';
BEFORE: 'before';
AFTER: 'later';
QUESTIONMARK: '?';
COMMA : ',';

SYMP:'cramps'| 'bloating'| 'stomachache'| 'fatigue'|'headache'|'nausea'|'diarrhea';
PER: 'period';
OVU: 'ovulation';
FER: 'fertile';
NONF: 'non-fertile';
CYCLE: 'cycle';
MO: 'month'|'months';
DAYS: 'days';
NUMBER: [0-9]+;
SLASH : '-';

WORD: [a-z]+;

WS: [ \t\r\n]+ -> skip;