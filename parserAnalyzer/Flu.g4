grammar Flu;     

program: sentence;

sentence: require | ask;

require: verb (phrase)? (ON|IN)? (date)?;

ask: WHAT (IS)? TM? (cycleStatus | specificPharse) QUESTIONMARK;

verb: START | END | SHOW;

phrase: (OVU | PER | FER | NONF)  CYCLE;

cycleStatus: CYCLE STATUS (ON|IN)? date;

specificPharse : (OVU | PER | FER | NONF) (DAYS)? (ON|IN)? dateMonth;

date: dateInNum | dateNumAndWord | dateInWord | dateCompare;

dateInNum: DATE_MONTH SLASH DATE_MONTH (SLASH YEAR)?;
dateNumAndWord: DATE_MONTH MONTH (YEAR)?;
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

SLASH : '/'|'-';

NUMBER: [0-9]+;
DATE_MONTH: INT | INT INT;
YEAR: INT INT INT INT;
INT: [0-9];


MONTH: 'JAN'| 'FEB'| 'MAR'| 'APRIL'|'MAY'|'JUNE'|'JULY'|'AUG'|'SEP'|'OCT'|'NOV'|'DEC';
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

ON: 'on';
IN: 'in';

WHEN: 'this'|'previous'|'next';

WORD: [a-z]+;

WS: [ \t\r\n]+ -> skip; 