// You can edit this code!
// Click here and start typing.
package main

import (
	"errors"
	"fmt"
)

type Encoder interface {
	Encode(val any) (string, error)
}

type FooEncoder struct{}

func (enc FooEncoder) Encode(val any) (string, error) {
	return fmt.Sprintf("%v is now a foo", val), nil
}

func NewFooEncoder() Encoder {
	return FooEncoder{}
}

type BarEncoder struct{}

func (enc BarEncoder) Encode(val any) (string, error) {
	return fmt.Sprintf("%v is now a bar", val), nil
}

func NewBarEncoder() Encoder {
	return BarEncoder{}
}

type ErrEncoder struct{}

func (enc ErrEncoder) Encode(val any) (string, error) {
	return "", fmt.Errorf("%v is now an error", val)
}

func NewErrEncoder() Encoder {
	return ErrEncoder{}
}

type EncoderConstructor func() Encoder

var reg = make(map[string]EncoderConstructor)

func MustRegister(name string, ctor EncoderConstructor) {
	if _, ok := reg[name]; ok {
		panic(name + " already registered")
	}
	reg[name] = ctor
}

// NewEncoder is a factory function that returns a new instance of an encoder
// of the specified type.
func NewEncoder(name string) (Encoder, error) {
	ctor, ok := reg[name]
	if !ok {
		return nil, errors.New(name + " is not registered")
	}
	return ctor(), nil
}

func main() {
	MustRegister("foo", NewFooEncoder)
	MustRegister("bar", NewBarEncoder)
	MustRegister("err", NewErrEncoder)

	val := "val"
	enc, _ := NewEncoder("foo")
	fmt.Println(enc.Encode(val))
	enc, _ = NewEncoder("bar")
	fmt.Println(enc.Encode(val))
	enc, _ = NewEncoder("err")
	fmt.Println(enc.Encode(val))

	// An error is expected here.
	enc, err := NewEncoder("baz")
	if err != nil {
		panic(err)
	}
}
