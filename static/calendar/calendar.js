// Create an enumeration.
function Enum(...names) {
	const result = {
		count: names.length,
		names: Object.freeze(names),
	};
	
	for (const value in names) {
		result[names[value]] = parseInt(value);
	}
	
	return Object.freeze(result);
}

// A day of a week.
const Day = Enum("MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN");

// A month of a year.
const Month = Enum(
	"JAN",
	"FEB",
	"MAR",
	"APR",
	"MAY",
	"JUN",
	"JUL",
	"AUG",
	"SEP",
	"OCT",
	"NOV",
	"DEC",
);

// Return whether a year is a leap year.
function isYearLeap(year) {
	return year % 400 === 0 || year % 4 === 0 && year % 100 !== 0;
}

// Get the length of a month in a year.
function getMonthLength(year, month) {
	switch (month) {
		case Month.APR:
		case Month.JUN:
		case Month.SEP:
		case Month.NOV:
			return 30;
		case Month.FEB:
			return isYearLeap(year) ? 29 : 28;
		default:
			return 31;
	}
}

// The current year on the calendar.
var currentYear = 2024;

// The current month on the calendar.
var currentMonth = Month.JAN;

// The day at the start of the current month on the calendar.
var startDay = Day.MON;

// Increment the current month.
function incrementMonth() {
	startDay = (startDay + getMonthLength(currentYear, currentMonth)) % Day.count;
	
	if (++currentMonth > Month.DEC) {
		currentMonth = Month.JAN;
		currentYear++;
	}
}

// Decrement the current month.
function decrementMonth() {
	if (--currentMonth < Month.JAN) {
		currentMonth = Month.DEC;
		currentYear--;
	}
	
	startDay = (startDay - getMonthLength(currentYear, currentMonth)) % Day.count;
	
	if (startDay < 0) {
		startDay += Day.count;
	}
}

// Increment the current year.
function incrementYear() {
	for (let i = 0; i < Month.count; i++) {
		incrementMonth();
	}
}

// Decrement the current year.
function decrementYear() {
	for (let i = 0; i < Month.count; i++) {
		decrementMonth();
	}
}

// Render the calendar to the document.
function renderCalendar() {
	document.getElementById("month").value = Month.names[currentMonth];
	document.getElementById("year").value = currentYear;
	
	const cells = document.querySelectorAll("#calendar td");
	const monthLength = getMonthLength(currentYear, currentMonth);
	
	for (let i = 0; i < cells.length; i++) {
		const cell = cells[i];
		
		if (i < startDay || i >= startDay + monthLength) {
			cell.classList.add("disabled");
			cell.innerText = "";
		} else {
			cell.classList.remove("disabled");
			cell.innerText = `${i - startDay + 1}`;
		}
	}
}

// Set the current date.
function setDate(month, year) {
	while (currentYear < year) {
		incrementYear();
	}
	
	while (currentYear > year) {
		decrementYear();
	}
	
	while (currentMonth < month) {
		incrementMonth();
	}
	
	while (currentMonth > month) {
		decrementMonth();
	}
	
	renderCalendar();
}

// Called when the month is changed. Set the current month.
function onMonthChanged(event) {
	setDate(Month[event.target.value], currentYear);
}

// Called when the year is changed. Set the current year.
function onYearChanged(event) {
	const year = parseInt(event.target.value);
	
	if (!isNaN(year)) {
		setDate(currentMonth, year);
	}
}

// Main function. Set the calendar and connect input events to the script.
function main() {
	const date = new Date();
	setDate(date.getMonth(), date.getFullYear());
	
	document.getElementById("month").addEventListener("change", onMonthChanged);
	document.getElementById("year").addEventListener("change", onYearChanged);
}

// Call the main function when the document is ready.
if (document.readyState === "complete" || document.readyState === "interactive") {
	setTimeout(main, 1);
} else {
	document.addEventListener("DOMContentLoaded", main);
}
