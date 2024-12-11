program S1_1a;

var
	Count, Total, Number : Integer;
	
begin
	Count := 1;
	Total := 0;
	repeat
		read(Number);
		if (Number>0) and (Number <20) then
			Total := Total+Number;
		Count := Count+1;
	until (Count > 5);
	write(Total);
end.
