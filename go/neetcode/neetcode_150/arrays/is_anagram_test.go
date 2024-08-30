package arrays

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func Test_IsAnagram(t *testing.T) {
	tests := []struct {
		s1, s2 string
		want         bool
	}{
		{
			s1: "racecar",
			s2: "carrace",
			want: true,
		},
		{
			s1: "racecar",
			s2: "racecar",
			want: true,
		},
		{
			s1: "jar",
			s2: "jam",
			want: false,
		},
		{
			s1: "jabba",
			s2: "foo",
			want: false,
		},
		{
			s1: "jabbathehut",
			s2: "hetuthbbjaa",
			want: true,
		},
		{
			s1: "jabbathehut",
			s2: "jabbathehuu",
			want: false,
		},
		{
			s1: "jaar",
			s2: "jarr",
			want: false,
		},
	}
	for _, tt := range tests {
		t.Run(
			tt.s1 + "_" + tt.s2,
			func(t *testing.T) {
				require.Equal(t, tt.want, IsAnagram(tt.s1, tt.s2))
				require.Equal(t, tt.want, IsAnagramSort(tt.s1, tt.s2))
			},
		)
	}
}
