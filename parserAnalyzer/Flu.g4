grammar Flu;     

program: sentence;

sentence: require | ask | checkStats | symptom;

symptom: dateInWord I FEEL symp;

symp : (SYMP COMMA symp) | SYMP ;

SYMP:'cramps'| 'bloating'| 'stomachache'| 'fatigue'|'headache'|'nausea'|'diarrhea';

COMMA : ',';

checkStats: CHECK CYCLE STATS;

require: verb (phrase)? (ON|IN)? (date)?;

ask: WHAT (IS)? TM? (cycleStatus | specificPharse) QUESTIONMARK;

verb: START | END | SHOW;

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

WHAT: 'what'|'What';

TM: THE|MY;

IS: 'is';
THE: 'the';
MY: 'my';

STATUS: 'status';

BeforeAfter: BEFORE|AFTER;

BEFORE: 'before';
AFTER: 'later';

SLASH : '-';

NUMBER: [0-9]+;

MO: 'month'|'months';

DAYS: 'days';

QUESTIONMARK: '?';

PER: 'period';
OVU: 'ovulation';
FER: 'fertile';
NONF: 'non-fertile';
CYCLE: 'cycle';

START: 'start'| 'Start';
END: 'End'| 'end';
SHOW: 'show'| 'Show';

CHECK:'check'| 'Check';
STATS: 'statistic';

ON: 'on';
IN: 'in';

WHEN: 'this'|'previous'|'next';
I :'i';
FEEL : 'feel';

WORD: [a-z]+;

WS: [ \t\r\n]+ -> skip; 