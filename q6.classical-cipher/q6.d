import std.stdio;
import std.array;
import std.algorithm;
import std.ascii;

void main()
{
	const s = "fsdz{Fdhvdu_flskhu_lv_fodvvlfdo_flskhu}";
	foreach (c; s)
	{
		if (!c.isAlpha)
			c.write;
		else if ((c - 3).isAlpha)
			write(cast(char)(c - 3));
		else
			write(cast(char)(c - 3 + 26));
	}
}
