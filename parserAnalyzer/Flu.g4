grammar Flu;     

program: sentence;

sentence: require | ask;

require: verb (phrase)? (ON)? (date)?;

ask: WHAT (IS)? TM (cycleStatus | specificPharse) QUESTIONMARK;

TM: THE|MY;

verb: START| END| SHOW;

phrase: (OVU | PER | FER | NONF)  CYCLE;

STATUS: 'status';

date: dateInNum | dateInWord | dateNumAndWord | dateCompare; 

dateNumAndWord: DATE_MONTH MONTH (YEAR)?;

dateInNum: DATE_MONTH SLASH DATE_MONTH (SLASH YEAR)?;

dateInWord: 'tomorrow'|'today'|'yesterday';

dateCompare: Number DAYS BeforeAfter;

WHAT: 'what'|'What';

IS: 'is';

THE: 'the';

cycleStatus: CYCLE STATUS (ON)? date;

specificPharse : (OVU | PER | FER | NONF) (DAYS)? (ON)? dateMonth;

Number: INT;

DAYS: 'days';

BeforeAfter: BEFORE|AFTER;

BEFORE: 'before';

AFTER: 'later';

MONTH: 'JAN'| 'FEB'| 'MAR'| 'APRIL'|'MAY'|'JUNE'|'JULY'|'AUG'|'SEP'|'OCT'|'NOV'|'DEC';

SLASH : '/'|'-';

WORD: [a-z]+;

DATE_MONTH: INT | INT INT;

YEAR: INT INT INT INT;

INT: [0-9]+;

QUESTIONMARK: '?';

dateMonth: monthWord| monthCompare;

monthWord: WHEN MO;

WHEN: 'this'|'previous'|'next';

monthCompare: Number MO BeforeAfter;

MO: 'month'|'months';

PER: 'period';

OVU: 'ovulation';

FER: 'fertile';

NONF: 'non-fertile';

CYCLE: 'cycle';

START: 'start'| 'Start';

END: 'End'| 'end';

SHOW: 'show'| 'Show';

ON: 'on';

MY: 'my';

WS: [ \t\r\n]+ -> skip; 
