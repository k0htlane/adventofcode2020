#include <assert.h>
#include <algorithm>
#include <iostream>
#include <vector>
#include <chrono>
#include <array>

using namespace std;

#define MAXCUPS 1000000
#define SPLIT 10000

class Cups;
Cups *first = NULL;

array<Cups*, MAXCUPS> owner;

class Cups
{
public:
	Cups *next;
	vector<int> cups;
	Cups(int size, int start=0):
		next(0)
	{
		if (size > SPLIT)
		{
			next = new Cups(size - SPLIT, start + SPLIT);
			size = SPLIT;
		}
		cups.resize(size);
		for(int i = 0; i < size; i++)
		{
			cups[i] = start+i;
			owner[start+i] = this;
		}
	}

	int operator[](int index)
	{
		if (index >= cups.size())
		{
			assert(next);
			return (*next)[index - cups.size()];
		}
		return cups[index];
	}

	vector<int> take(int index, int count = 3)
	{
		if (index >= cups.size())
		{
			// assert(next);
			if (!next)
				return first->take(index - cups.size(), count);
			return next->take(index - cups.size(), count);
		}
		vector<int> ret;
		while (count-- && index < cups.size())
		{
			ret.push_back(cups[index]);
			cups.erase(cups.begin() + index);
		}
		if (count != -1)
		{
			auto children = next ? next->take(0, count+1) : first->take(0, count+1);
			ret.insert(ret.end(), children.begin(), children.end());
		}

		if (cups.empty() && next)
		{
			cups = next->cups;
			next = next->next; // TODO delete old
			for (auto i: cups)
				owner[i] = this;
		}
		if (next && next->cups.empty())
		{
			next = next->next; // TODO delete old
		}

		return ret;
	}

	void place(int index, vector<int> values)
	{
		if (index > cups.size())
		{
			assert(next);
			next->place(index - cups.size(), values);
			return;
		}
		if (cups.size() > 2*SPLIT && index > 0)
		{
			auto nextnext = next;
			next = new Cups(0);
			next->next = nextnext;
			next->cups.insert(next->cups.begin(), cups.begin()+index, cups.end());
			for (auto v: next->cups)
				owner[v] = next;
			cups.resize(index);
			assert(index == cups.size());
			next->place(0, values);
		}
		else
		{
			cups.insert(cups.begin() + index, values.begin(), values.end());
			for (auto i: values)
				owner[i] = this;
		}
	}

	int index(int value)
	{
		if (this != owner[value])
		{
			assert(next);
			return next->index(value) + cups.size();
		}
		auto pos = find(cups.begin(), cups.end(), value);
		return pos - cups.begin();
	}

	int size()
	{
		int ret = cups.size();
		if (next)
			ret += next->size();
		return ret;
	}
};

bool has(vector<int> vec, int val)
{
	assert(vec.size() == 3);
	return vec[0] == val || vec[1] == val || vec[2] == val;
}


int main()
{
	Cups cups(MAXCUPS);
	first = &cups;
	string s;
	cin >> s;

	for (int i = 0; i < s.length(); i++)
		cups.cups[i] = s[i] - '1';


	int current = 0;
	auto t0 = chrono::steady_clock::now();
	for (int i = 0; i < 10000000; i++)
	{
		auto cup = cups[current];
		auto picked_up = cups.take(current+1);
		int dest = cup-1;
		if (dest < 0) dest = MAXCUPS-1;
		while (has(picked_up, dest))
		{
			dest --;
			if (dest < 0) dest = MAXCUPS-1;
		}
		cups.place(cups.index(dest)+1, picked_up);
		current = (cups.index(cup)+1) % MAXCUPS;
		assert(cups.size() == MAXCUPS);

		if (i % 100000 == 0 && i)
		{
			chrono::duration<double> dt = chrono::steady_clock::now() - t0;
			t0 = chrono::steady_clock::now();
			cout << i/100000 << "00K " << dt.count() << " ETA: " << dt.count() / 100000 * (10000000 - i)<< endl;
		}
	}
	cout << "Finished" << endl;
	current = cups.index(0);
	auto a = cups[current+1]+1;
	auto b = cups[current+2]+1;
	cout << a << " * " << b << " = " << a*b << endl;

	return 0;
}